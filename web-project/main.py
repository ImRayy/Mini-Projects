from crypt import methods
import math
from flask import Flask, render_template, request, session, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_mail import Mail
import json



## Opeaning config file for easy customizaion ##
slno = []

with open("config.json", "r") as config:

    home_page = json.load(config)["home"]

with open("config.json", "r") as config:
    about_page = json.load(config)["about"]

# with open('config.json', 'r') as config:
#     post_page = json.load(config)["post"]

with open("config.json", "r") as config:
    contact_page = json.load(config)["contact"]

with open("config.json", "r") as config:
    login_page = json.load(config)["loginpage"]


web = Flask(__name__)
web.secret_key = "super-secret-key"
web.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


# Flask mail ( for more info visit https://pythonhosted.org/Flask-Mail/)
web.config.update(
    MAIL_SERVER="smtp.gmail.com",
    MAIL_PORT=465,
    MAIL_USERNAME=contact_page["mailid"],
    MAIL_PASSWORD=contact_page["password"],
    MAIL_USE_TLS=False,
    MAIL_USE_SSL=True,
)
mail = Mail(web)

# Mysql database url, it's diffrent for linux and windows, mac os, for windows "mysql+pymysql://root:hellblade@localhost/anime_otaku"
web.config[
    "SQLALCHEMY_DATABASE_URI"
] = "mysql+pymysql://root:hellblade@localhost/anime_otaku?unix_socket=/opt/lampp/var/mysql/mysql.sock"
db = SQLAlchemy(web)


## Database Classes ##


class Contacts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone_no = db.Column(db.String(120), nullable=False)
    msg = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(120))


class Posts(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60), nullable=False)
    author = db.Column(db.String(30), nullable=False)
    slug = db.Column(db.String(25), nullable=False)
    content = db.Column(db.String(5000), nullable=False)
    date = db.Column(nullable=False)
    img_file = db.Column(db.String(15), nullable=False)


# class Post(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     name = db.Column(db.String(80), unique=True)
#     email = db.Column(db.String(120), unique=True)
#     phone_no = db.Column(db.String(120), unique=True)
#     msg = db.Column(db.String(120), unique=True)
#     date = db.Column(db.String(120), unique=True)


## Loading webpages through flask and setting route/path/address ##
def add_to_dict(dict_obj, key, value):
    # Check if key exist in dict or not
    if key in dict_obj:
        # Key exist in dict.
        # Check if type of value of key is list or not
        if not isinstance(dict_obj[key], list):
            # If type is not list then make it list
            dict_obj[key] = [dict_obj[key]]
        # Append the value in list
        dict_obj[key].append(value)
    else:
        # As key is not in dict,
        # so, add key-value pair
        dict_obj[key] = value


@web.route("/")
def home():
    post = Posts.query.filter_by().all()
    #[0 : int(home_page["number_of_posts"])]
    last = math.ceil(len(post)/int(home_page["number_of_posts"]))
    page = request.args.get('page')
    if not str(page).isnumeric():
        page = 1
    page = int(page)
    post = post[(page - 1)*int(home_page["number_of_posts"]):(page - 1)*int(home_page["number_of_posts"]) + int(home_page["number_of_posts"]) ]

    if page == 1:
        prev = "#"
        next = "/?page=" + str(page+1)
    elif page == last:
        prev = "/?page=" + str(page-1)
        next = "#"
    else:
        prev = "/?page=" + str(page - 1)
        next = "/?page=" + str(page + 1)
    
    return render_template("index.html", home=home_page, post_content=post, next = next, prev = prev)


@web.route("/login", methods=["GET", "POST"])
def login():

    if "user" in session and session["user"] == login_page["admin_username"]:
        post = Posts.query.filter_by().all()
        return render_template("dashboard.html", post_content = post)

    if request.method == "POST":
        username = request.form.get("uname")
        userpass = request.form.get("pass")
        if (
            username == login_page["admin_username"]
            and userpass == login_page["admin_password"]
        ):
            add_to_dict(session, "user", login_page["admin_username"])
            add_to_dict(session, "logged_in", True)
            post = Posts.query.filter_by().all()
            return render_template("dashboard.html", post_content = post)

    return render_template("login.html", loginPage = login_page)

@web.route("/logout", methods=['GET', 'POST'])
def logout():
    session.pop('user')
    return redirect('/login')
        

@web.route("/about")
def about():
    return render_template("about.html", about=about_page)


@web.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        phone = request.form.get("phone_no")
        message = request.form.get("message")

        entry = Contacts(
            name=name, email=email, phone_no=phone, msg=message, date=datetime.now()
        )
        mail.send_message(
            "Anime Otaku: message from " + name,
            sender=email,
            recipients=["sanjuroy741254@gmail.com"],
            body=f"{message} \n\n By {name}\n\nPhone No.{phone}",
        )

        db.session.add(entry)
        db.session.commit()
        mail.send_message(
            "From Anime Otaku Team",
            sender="1rayunlikechaser@keemail.me",
            recipients=[str(email)],
            body=f"Hi {name} Hope you have been enjoying our posts so far. We want to continue offering the best posts. Could you please take few seconds and share our posts?, and also give your valuable feedback more, Please be honest with your responses. If you don't like something, do not be afraid to point it out. We take feedback very seriously and are ready to make changes to help serve you better. \n\nThank you,\nSouradeep Roy",
        )

    return render_template("contact.html", contact=contact_page)


@web.route("/post/<string:post_slug>", methods=["GET"])
def post_page(post_slug):

    post = Posts.query.filter_by(slug=post_slug).first()

    return render_template("post.html", post_content=post)

@web.route("/edit/<string:post_sno>" , methods=['GET', 'POST'])
def post_edit(post_sno):
   
    if "user" in session and session["user"] == login_page["admin_username"]:
        if request.method=="POST":
            post_title = request.form.get('title')
            post_author = request.form.get('author')
            post_slug = request.form.get('slug')
            post_imgFile = request.form.get('img_file')
            post_content = request.form.get('content')
            date = datetime.now()
            if post_sno != '0':
              
                post = Posts.query.filter_by(sno=post_sno).first()
                post.title = post_title
                post.author = post_author
                post.slug = post_slug
                post.content = post_content
                post.img_file = post_imgFile
                post.date = date
                db.session.commit()
                db.session.execute()
                return redirect('/edit/'+post_sno)
                
            else:
                post = Posts(title=post_title, author = post_author, slug = post_slug, content = post_content, img_file = post_imgFile,  date=date)
                db.session.add(post)
                db.session.commit()
                            
                
    
    post = Posts.query.filter_by(sno = post_sno).first()
    return render_template('edit.html',  post = post, postsno = post_sno)
    
@web.route("/delete/<string:post_sno>", methods = ['GET', 'POST'])
def post_delete(post_sno):
    if "user" in session and session["user"] == login_page["admin_username"]:
        post = Posts.query.filter_by(sno=post_sno).one()
        db.session.delete(post)
        db.session.commit()
        return redirect('/login')

if __name__ == "__main__":

    web.run(debug=True)

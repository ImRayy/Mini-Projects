from stdiomask import getpass
from colorama import Fore
import hashlib

def register():
    dont_write = 0
    print(
        "Register",
        "\n------------",
    )
    while True:
        user_fullname = input("Enter your full name-> ")
        if user_fullname != " ":
            break
    user_fullname = beautifyWords(user_fullname)

    while True:
        user_name = input("Enter your user name-> ")
        if checkIfGenuine(user_name) == True:
            print("Space and special characters not supported", "\n")
        elif checkUserExistance(user_name) == True:
            print(Fore.LIGHTBLUE_EX)
            print("Username not available,try something diffrent", "\n")
            print(Fore.RESET)
        else:
            break
    while True:
        user_pass = getpass("Enter your password-> ")
        if user_pass != "":
            break
    i = 0
    while True:
        i += 1
        user_pass_confrm = getpass("Confirm your password-> ")
        if user_pass == user_pass_confrm:
            dont_write = 1
            break
        elif user_pass != user_pass_confrm and i == 3:
            i = 0
            userDontExistText()
            break
        else:
            print(Fore.RED)
            print("Password don't match, try again")
            print(Fore.RESET)
    if dont_write == 1:
        addToDatabase([user_name, encodePass(user_pass), user_fullname])
        return True


def checkIfGenuine(user_fullname):

    if " " in user_fullname:
        return True
    else:
        return False


def login():
    g = 0
    dont_write = False
    print(Fore.LIGHTYELLOW_EX)
    print("LOGIN", "\n------------")
    print(Fore.RESET)
    userCredentials = {}
    with open(".database.txt") as file:
        for content in file:
            content = content.split(" ")
            userCredentials.update({content[0]: content[1]})

        user_name = input("Enter your username-> ")
        i = 0
        while True:
            if user_name in userCredentials:
                while True:
                    i = i + 1
                    user_pass = getpass("Enter your password-> ")
                    if passCheck(user_pass, userCredentials[user_name]) == True:
                        i == 0
                        dont_write = True
                        break

                    elif i == 3 :
                        i = 0
                        userDontExistText()
                        break
                    else:
                        print(Fore.RED)
                        print("Incorrect Password!")
                        print(Fore.RESET)
                break
            else:
                userDontExistText()
                break


    if dont_write == True:
        userFullName = content[2]
        userFullName = userFullName.replace("-", " ")
        print(Fore.LIGHTGREEN_EX)
        print("Login successfull!", Fore.RESET)
        print("Welconme back", userFullName)
        return [True,user_name]
    return [False,user_name]

def give_access():
    if login() == True:
        return True

def checkUserExistance(user_name):
    with open(".database.txt") as file:
        for content in file:
            content = content.split(" ")
            if content[0] == user_name:
                return True


def userDontExistText():
    print(Fore.RED)
    print("User don't exist", Fore.LIGHTYELLOW_EX, "\n")
    print("For register input 'R/r'", "To Login input 'L/l","To Quit input 'Q/q'")
    print(Fore.RESET)
    while True:
        user_input = input("-> ").lower()
        if user_input == "r":
            register()
            break
        elif user_input == "l":
            login()
            break
        elif user_input == 'q':
            break
        else:
            print(Fore.RED)
            print("Invalid Input!")
            print(Fore.RESET)


def addToDatabase(user_name: list):
    with open(".database.txt", "a") as file:
        for data in user_name:
            file.write(data)
            file.write(" ")
        file.write("\n")


def beautifyWords(user_name):
    user_name = user_name.split()
    user_name = "-".join(user_name)
    return user_name


def encodePass(password):
    return hashlib.sha256(str.encode(password)).hexdigest()


def passCheck(user_password, hash):
    if encodePass(user_password) == hash:
        return True
    else:
        return False


# def changePassword():
#     pass

# def deleteAccount():
#     pass

def main():
    print(Fore.LIGHTYELLOW_EX)
    print(
        "Welcome",
        "\n------------",
        "\n1. Register",
        "\n2. Login",
        "\n------------",
    )
    print(Fore.RESET)

    # giving functions
    while True:
        user_input = input("-> ")
        print()

        if user_input in ["1", "2", "3", "4"]:
            break

        else:
            print(Fore.RED)
            print("Invalid Input, enter again")
            print(Fore.RESET)


    if user_input == "1":
        register()

    elif user_input == "2":
        login()
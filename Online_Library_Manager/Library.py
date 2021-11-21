#modules
from os import name, read, replace, write
from colorama.ansi import Fore, code_to_chars
import loginSystem
import libraryFunctions
#classes
class Library:
    def __init__(self,library_name,all_books = None):
        self.library_name = library_name
        if all_books is None:
            all_books = []
        self.all_books = all_books




    @staticmethod
    def listofbooks (self):
        print ()


#loginSystem
grant_permission = ' '
creater_browesr = ' '
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
    loginSystem.register()

elif user_input == "2":
    grant_permission = loginSystem.login()

user_name = grant_permission[1]

#Grant Permssoin

print("1. Manage your library","2. Browse Library") if grant_permission[0] == True else print(" ")
while True and grant_permission[0] == True:
    creater_browesr = input("-> ")
    if creater_browesr in ['1','2']:
        break

# Blank Variables

#  0
bookList = []
userName = user_name
breakTime = 0
#Gives acess to inputes

if creater_browesr == '1' and grant_permission[0] == True:
    print("1. Create new library", "\n2. Update book list", "\n3. Delete book/books from list", "\n4. Review your books")
    userChoise = input("-> ")
    while True:
        if userChoise in ['1','2','3','4']:
            break
        else:
            print("Not valid input")
            print()
    
    if userChoise == '1':
        
        if libraryFunctions.checkLibraryExistance(user_name) == True:
            print("A library already associated with your account, you can't create more")
           
        else:
            creater_libraryName = input("Enter your library name you want to give-> ")
            #libraryName = creater_libraryName
            print("Enter books names you want to include")
            libraryFunctions.addToLibrary(bookList)
            libraryFunctions.addToDatabase(user_name,creater_libraryName,bookList)
            breakTime = 1
    
    elif userChoise == '2':
        with open (".library.txt") as file:
            for content in file:
                content = content.split(" ")
                if content[0] == user_name:
                    bookList = list(content[2].split("-"))
                    print("Enter books you want to add to your library")
                    libraryFunctions.addToLibrary(bookList)
                    libraryFunctions.updateDatabase(content[2],bookList)
                else :
                    print("Library don't exist, create a library first")

    elif userChoise == '3':
        with open (".library.txt") as file:
            for content in file:
                content = content.split(" ")
                if content[0] == user_name:
                    bookList = list(content[2].split("-"))
                    print("Enter books you want to add to your library")
                    libraryFunctions.deleteFromLibrary(bookList)
                    libraryFunctions.updateDatabase(content[2],bookList)
                else :
                    print("Library don't exist, create a library first")
    elif userChoise == '4':
        with open(".library.txt") as file:
            for content in file:
                content = content.split(" ")
            if content[0] == user_name:
            
                books = content[2]
                books = list(content[2].split("-"))
                for item in books:
                    print(item)
            else :
                print("Library don't exist, create one first")
           
    userName = Library(creater_libraryName,bookList) if breakTime == 1 else print(" ")
            
# Library browser/user
elif creater_browesr == '2' and grant_permission[0] == True:
    pass
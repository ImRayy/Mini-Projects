# modules
import fileinput
from os import curdir, name, path, read, replace, write
from colorama import Fore
import loginSystem

import ast
import time
from pathlib2 import Path
# Functions
def addToLibrary(bookList):
    while True:
        booklistInput = input("-> ")
        if booklistInput == 'quit':
            break
        else:
            bookList.append(booklistInput)
            bookList.sort()

def deleteFromLibrary(bookList):
    while True:
        booklistInput = input("-> ")
        if booklistInput == 'quit':
            break
        else:
            bookList.remove(booklistInput)
            bookList.sort()

def addToDatabase(userName,libraryName,boolList):
    with open (".library.txt", 'a+') as file:
        file.write(userName)
        file.write("-")
        file.write(libraryName)
        file.write("-")
        file.write(str(boolList))
        file.write("\n")

def updateDatabase(prvlist,currentlist):
    
    with Path(".library.txt") as file:
        content = file.read_text()
        content = content.replace(str(prvlist), str(currentlist))
        file.write_text(content)

def checkLibraryExistance(user_name):
    with open(".library.txt") as file:
        for content in file:
            content = content.split(" ")
            if content[0] == user_name:
                return True

def displayallbooks():
    with open(".library.txt") as file:
        for content in file:
            content = content.split(" ")
            for books in content[2]:
                books = list(books.split("-"))
                print (books)

def listOfLibrary():
    print()
    with open (".library.txt") as file:
        for item in file:
            if item != None:
                item = item.split("-")
                print(item[1])
        print()
def listOfbooks():
    with open (".library.txt") as file:
        for content in file:
            content = content.split("-")
            books = ast.literal_eval(content[2])
            dict(books)

        return books
def booklibraryHistroy(libraryName):
    with open(".lenderDB.txt") as file:
        for item in file:
            item = item.split("-")
            if item[0] == libraryName:
                prev = ast.literal_eval(item[1])
                print(True)
                return [True,prev]
    return [False,None]
        





# classes


class Library:
    def __init__(self, library_name, all_books=None):
        self.library_name = library_name
        if all_books is None:
            all_books = []
        self.all_books = all_books
        self.lendbooks = {}

    def showBooks(self):
        print(f"List of all books of {self.library_name}")
        for items in self.all_books:
            print(items)

    def lendBooks(self, book, user):
        x = booklibraryHistroy(self.library_name)

        if x[0] == True:
            self.lendbooks.update(x[1])
            if book not in self.lendbooks.keys():
                self.lendbooks.update({book: user})
                with Path(".lenderDB.txt") as file:
                    item = file.read_text()
                    item  = item.replace(str(x[1]), str(self.lendbooks))
                    file.write_text(item)
                    print("Database successfully updated, you may take your book now")
            else:
                userFullname = self.lendbooks[book]
                with open (".library.txt") as file:
                    for item in file:
                        item = item.split("-")
                    
                print(f"Book you're looking for is currently lended by {self.lendbooks[book]}")

        else:
            self.lendbooks.update({book: user})
            with open(".lenderDB.txt", "a") as file:
                file.write(self.library_name)
                file.write("-")
                file.write(str(self.lendbooks))
                file.write("\n")

    def displayAvailableBooks(self, books):
        time.sleep(2)
        with open (".lenderDB.txt") as file:
            for item in file:
                item = item.split("-")
                dbBooks = ast.literal_eval(item[1])
                self.lendbooks.update(dbBooks)
        for book in books:
            if book not in self.lendbooks.keys():
                print(book)
    
    def returnBook(self, returnInput):
        with open (".lenderDB.txt") as file:
            for item in file:
                item = item.split("-")
                prevbook = ast.literal_eval(item[1])
        self.lendbooks.update(prevbook)
        self.lendbooks.pop(returnInput)
        with Path(".lenderDB.txt") as file:
            item = file.read_text()
            item = item.replace(str(prevbook), str(self.lendbooks))
            file.write_text(item)

    def donateBook(self,donate):
        prevList = self.all_books.copy()
        self.all_books.append(donate)
        currentList = self.all_books.copy()
        updateDatabase(prevList, currentList)


# loginSystem
grant_permission = " "
creater_browesr = " "
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

# Grant Permssoin

print("1. Manage your library", "2. Browse Library") if grant_permission[
    0
] == True else print(" ")
while True and grant_permission[0] == True:
    creater_browesr = input("-> ")
    if creater_browesr in ["1", "2"]:
        break

# Blank Variables

#  0
bookList = []
userName = user_name
breakTime = 0
# Gives acess to inputes

if creater_browesr == "1" and grant_permission[0] == True:
    print(
        "1. Create new library",
        "\n2. Update book list",
        "\n3. Delete book/books from list",
        "\n4. Review your books",
    )
    userChoise = input("-> ")
    while True:
        if userChoise in ["1", "2", "3", "4"]:
            break
        else:
            print("Not valid input")
            print()

    if userChoise == "1":

        if checkLibraryExistance(user_name) == True:
            print(
                "A library already associated with your account, you can't create more"
            )

        else:
            creater_libraryName = input(
                "Enter your library name you want to give-> ")
            # libraryName = creater_libraryName
            print("Enter books names you want to include")
            addToLibrary(bookList)
            addToDatabase(
                user_name, creater_libraryName, bookList)
            breakTime = 1

    elif userChoise == "2":
        with open(".library.txt") as file:
            for content in file:
                if content != None:
                    content = content.split("-")
                    if content[0] == user_name:
                        currentbookList = ast.literal_eval(content[2])
                        prevlist = ast.literal_eval(content[2])
                        print("Enter books you want to add to your library")
                        addToLibrary(currentbookList)
                        updateDatabase(prevlist, currentbookList)
                        break
                    else:
                        print("Library don't exist, create a library first")

    elif userChoise == "3":
        with open(".library.txt") as file:
            for content in file:
                content = content.split("-")
                if content[0] == user_name:
                    prevlist = ast.literal_eval(content[2])
                    bookList = ast.literal_eval(content[2])
                    print("Enter books you want to delete from your your library")
                    deleteFromLibrary(bookList)
                    updateDatabase(prevlist, bookList)
                    break
                else:
                    print("Library don't exist, create a library first")
    elif userChoise == "4":
        with open(".library.txt") as file:
            for content in file:
                content = content.split("-")
                if content[0] == user_name:

                    books = content[2]
                    books = ast.literal_eval(content[2])
                    print()
                    for item in books:
                        print(item)
                    break
                else:
                    print("Library don't exist, create one first")

    userName = Library(creater_libraryName,
                       bookList) if breakTime == 1 else print(" ")

# Library browser/user
elif creater_browesr == "2" and grant_permission[0] == True:
    print("Choose which library you want to browse")
    listOfLibrary()
    chosenLibrary = input("-> ")
    with open(".library.txt") as file:
        for content in file:
            content = content.split("-")
            if content[1] == chosenLibrary:
                librarian = content[0]
                libraryName = content[1]
                bookList = ast.literal_eval(content[2])
                librarian = Library(libraryName, bookList)

    print(
        "0. Exit",
        "\n1. Display all books",
        "\n2. Display available books",
        "\n3. Lend book",
        "\n4. Return book",
        "\n5. Donate book",
    )
    while True:
        userInput = input("-> ")
        while True:
            if userInput in ["1", "2", "3", "4", "5", "0"]:
                break
            else:
                print(Fore.RED)
                print("Invalid Input")
                print(Fore.RESET)
                break

        if userInput == '0':
            break
        elif userInput == "1":
            librarian.showBooks()
        elif userInput == "2":
            librarian.displayAvailableBooks(bookList)
        elif userInput == "3":

            lendBook = input(
                "Enter book name you want to lend-> ").lower()
            if lendBook in bookList:
                librarian.lendBooks(lendBook, user_name)
                break
            else:
                print(
                    "Sorry! book is currently not available in your chosen library, you may request librarian to add")

        elif userInput == "4":
            returnInput = input("Enter bookname you want to return-> ")
            librarian.returnBook(returnInput)
        elif userInput == "5":
            donate = input("Enter bookname you want to donate-> ")
            librarian.donateBook(donate)

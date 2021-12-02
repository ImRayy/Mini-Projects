#Functions
import ast
import fileinput

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
    with fileinput.FileInput(".library.txt", inplace=True) as file:
        for item in file:
            print(item.replace(str(prvlist), str(currentlist)), end=" ")

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
    with open (".library.txt") as file:
        for content in file:
            content = content.split("-")
            for item in content[1]:
                print(item, end="")
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
        
pass
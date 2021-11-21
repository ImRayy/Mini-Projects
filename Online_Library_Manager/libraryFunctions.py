#Functions
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
    boolList = "-".join(map(str,boolList))
    with open (".library.txt", 'a+') as file:
        file.write(userName)
        file.write(" ")
        file.write(libraryName)
        file.write(" ")
        file.write(boolList)
        

def updateDatabase(prvlist,currentlist):
    currentlist = "-".join(map(str, currentlist))
    with fileinput.FileInput(".library.txt", inplace=True) as file:
        for item in file:
            print(item.replace(prvlist, currentlist), end=" ")

def checkLibraryExistance(user_name):
    with open(".library.txt") as file:
        for content in file:
            content = content.split(" ")
            if content[0] == user_name:
                return True



# import loginSystem

# x = loginSystem.login()
# # y = loginSystem.register()

# if x[0]== True:
#     print(x[1])

# elif x[0] == False :
#     print("Login Failed!")

# def main():
#     pass
# print("This is main menu")
# userInput = 0

# while True:
#     userInput = int(input("1 or 2-> "))
#     if userInput == 1:
#         print("This")
#     elif userInput == 2:
#         main()
#         break

# with open("test.txt") as file:
#     x = file.readline()
#     x = x.split("-")
# print(x)
# x.append("noway")
# print(x)
'''capatalize'''
# list3 = ["Into the mist","Fortune cookie","Dark witch in the jungle","A boy all alone in rainy night" ]
# print(type(list3))

# for item in list3:
#     item = item.split(" ")
#     for i in item:
#         i = i.capitalize()
#         print(i, end=" ")
#     print()
'''project file'''


from  fileinput import FileInput
import ast
from json import dump
from os import lseek
file1 = open(".library.txt")

# random = file1.readline()

# for content in file1:
#     content =  content.split("-")
#     for i in range(len(content)):
#         if i > 0:
#             print(content[i])

'''nenxt'''
# import fileinput
# file1 = open("test.txt")
# for shit in file1:
#     shit = shit.split(" ")
# bigshit =shit[1]
# print(type(shit[1]))


# with fileinput.FileInput("test.txt", inplace=True, backup='.bak') as file:
#     for line in file:
#         print(line.replace(bigshit, "sjot"), end='')


# file = open ("test.txt")
# for content in file:
#     content = content.split(" ")
#     list = content[2]

# list = list.replace("-", " ")
# print(list)


# list1 = list
# del list

# list1 = list(list1.split(" "))


# list1.remove("\n")
# print(list1)

'''read files of same column'''
# i = input("input something, anything-> ")
# with open ("test.txt") as file:
#     for content in file:
#         content = content.split()
#         if content[1] == i:
#             print(content[0])

'''dictionaty'''
# import pickle
# import json
# good = {'arch':'the best distro'}


# a_file = open("data.json", "w")

# json.dump(good, a_file)

# a_file.close()


# a_file = open("data.json", "r")

# output = a_file.read()

# print(output)
# from fileinput import FileInput
# import json
# import ast
# file =  open(".library.json") 
# for x in file:        
#     x = x.split("-")
#     noway = x[1]
#     print(noway)
# dictionary = ast.literal_eval(noway)
# print(type(dictionary))
# shit = {'GKGHKJ': 'HGJKHJ'}

# with FileInput(".library.json", inplace=True) as file:
#     for content in file:
#         print(content.replace(str(x[1]),str(shit)), end=" ")

from pathlib2 import Path

list1 = ['arch', 'debian', 'deepin','kde', 'lxqt', 'manjaro', 'plasma', 'xfce']
list2 = ['arch', 'debian', 'deepin','kde', 'lxqt', 'manjaro', 'plasma', 'xfce','gnome']

with Path(".library.txt") as file:
    data = file.read_text()
    data = data.replace(str(list1), str(list2))
    file.write_text(data)


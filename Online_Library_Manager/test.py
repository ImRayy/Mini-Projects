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


file = open ("test.txt")
for content in file:
    content = content.split(" ")
    list = content[2]

list = list.replace("-", " ")
print(list)


list1 = list
del list

list1 = list(list1.split(" "))

    
list1.remove("\n")
print(list1)
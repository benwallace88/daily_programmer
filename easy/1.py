# create a program that will ask the users name, age, and reddit username. have it tell them the information back, in the format:
# your name is (blank), you are (blank) years old, and your username is (blank)
# for extra credit, have the program log this information in a file to be accessed later.

iName = raw_input("Hello, what is your name? - ")
iAge = raw_input("What is your age? - ")
iUname = raw_input("What is your reddit username? - ")

outString = "your name is " + iName + ", you are " + iAge + " years old, and your username is " + iUname + "\n"

print(outString)

outFile = open("1storage.txt", "a")
outFile.write(outString)

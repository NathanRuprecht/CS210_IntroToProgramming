from datetime import datetime
from os.path import dirname
from random import random
from string import whitespace, punctuation
import cgi



DATA_FILE = dirname( __file__ ) + "\\" + "Students.txt"

filename = "Students.txt"

def dictmain(filename):
    words = {}

    with open(filename, "r") as data_file:
        for word in data_file.read().split(";"):
            word = word.strip(whitespace + punctuation)
            print(word[0])



def listmain(filename):
    data = open(filename, "r")

    fullname = []
    timespicked = []
    picture = []
    num_students = []

    for word in data:
        values = word.split(";")
        fullname.append(values[0])
        timespicked.append(values[1])
        picture.append(values[2])

    for i in range(len(fullname)):
        num_students.append(i)
        num_students[i] = i

    print(num_students)


    data.close()




listmain(filename)

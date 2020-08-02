import datetime
def getdate():
    return datetime.datetime.now()
def take():
    b = int(input("enter 1 for python classes \n enter 2 for python projects \n enter 3 for c clases \n enter 4 for c projects"))
    if b == 1:
        value = input("type here \n")
        with open("my python classes.txt", "a") as op:
            op.write(str([str(getdate())]) + ": " + value + "\n")
        print("sucessfully written")
    elif b == 2:
        value = input("type here \n")
        with open("my python project.txt", "a") as op:
            op.write(str([str(getdate())]) + ": " + value + "\n")
        print("sucessfully written")
    elif b == 3:
        value = input("type here \n")
        with open("my c tut.txt", "a") as op:
            op.write(str([str(getdate())]) + ": " + value + "\n")
        print("sucessfully written")
    elif b == 4:
        value = input("type here \n")
        with open("my c project.txt", "a") as op:
            op.write(str([str(getdate())]) + ": " + value + "\n")
        print("sucessfully written")
    else:
        print("invalid plz try again...")
def retrive():
    c = int(input("enter 1 for python classes \n enter 2 for python projects \n enter 3 for c clases \n enter 4 for c projects"))
    if c == 1:
        with open("my python classes.txt") as op:
            for i in op:
                print(i, end=" ")
    elif c == 2:
        with open("my python project.txt") as op:
            for i in op:
                print(i, end=" ")
    elif c == 3:
        with open("my c tut.txt") as op:
            for i in op:
                print(i, end=" ")
    elif c == 4:
        with open("my c project.txt") as op:
            for i in op:
                print(i, end=" ")
    else:
        print("invalid num.")
print("work management system: ")
d=int(input("type 1 for add text in data \n type 2 for read data "))
if d == 1:
    take()
elif d == 2:
    retrive()
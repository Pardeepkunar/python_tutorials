# exercise if else -> nested if else

name = 12
user = int(input("guess a number 1 t0 100 "))
if user == name:
    print(" you are win")
else:
    if user < name:
        print("to low")
    else:
        print("to high")    
# while exercise

name = input("eneter name")
temp = ""
a=0
while a <= len(name):
    if name[a] not in temp:
        temp = temp + name[a]
        print(f"{name[a]} : {name.count(name[a])}")
    a = a+1
    



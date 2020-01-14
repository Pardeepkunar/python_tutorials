# String_methor 
# replace()  methor
# find () methor

name = "pardeep is kumar is "
#print(name.replace(" ","_"))

a = name.find("is")
b= name.find("is",a+1)
print(b)

# center methor
deep ="pardeep"
print(deep.center(11,"*"))

# program center
deepi = input("enter : ")
print(deepi.center(len(deepi) + 4 , "*"))
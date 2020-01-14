# string methor()
# len() function
# lower() function
# upper() function
# title() function
# cout() function
#Strip_methor()

name = "pardeep"
print(len(name))

a= "pardeep KUMAR"
print(a.lower())

b ="pardeep KUMAR"
print(a.upper())

c ="pardeep KUMAR"
print(c.title())

d="prdeep Kumar"
print(d.count("e"))


#exercise

name1= input("enter name : ")
name2 =input("enter char : ")
print(len(name1))
print(name1.lower().count(name2.lower()))

# Sprit_methor()

deep = "     pardeep     "
deep1 = "................"
print(deep + deep1)
print(deep.lstrip() + deep1) # left side space remove
print(deep.rstrip() + deep1)
print(deep.strip() + deep1)
print(deep.replace(" ","") + deep1)
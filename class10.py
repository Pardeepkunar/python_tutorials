# String_index value

name ="pardeep"
print(name[0])
print(name[-3])

# string_ silicing
# syntax -> [start : stop]
name1 ="pardeep"
print(name1[0:4])
print(name1[:])
print(name1[1:])
print(name1[:3])
print("\n")


# step_argument_silicing
print("pardeep"[2:5])
print("pardeep"[0:7:2])
print("pardeep"[::2])
print("pardeep"[7::-1]) # back
print("pardeep"[-1::-1])

# exerciss
a = input("enter the name: ")
print(f"reverse number is {a[-1::-1]}")
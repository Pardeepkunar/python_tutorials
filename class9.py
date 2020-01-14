# string formating

a = "pardeep"
b = "20"
print("hello {} your age is {}".format(a,b))   # 3python
print(f"hello {a} your age is {b}")            # 3.6 python

# exercise

# num = input("enter 1 :")
# num1 = input("enter 2 :")
# num2 = input("enter 3 :")
num,num1,num2 = input("enter three number ").split(",")
print(f"total : {int(num) + int(num1) + int(num2)}")
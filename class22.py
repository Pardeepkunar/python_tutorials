# While loop

a = 1
while a<10:
    print(f"number : {a}")
    a = a+1

# program while

print("\n")
total = 0
a = 1
while a <= 10:
    total = total + a
    a =a+1
print(f"total sum is {total}")    

# program while
print("\n program 2")
total1 = 0
user1 = int(input("enter value: "))
b = 1
while b <= user1:
    total1 = total1 + b
    b =b+1
print(f"total sum is {total1}")  

# program while
print("\n program 3")
total1 = 0
user1 = input("enter value: ")
b = 0
while b < len(user1):
    total1 += int(user1[b])
    b =b+1
print(f"total sum is {total1}")  


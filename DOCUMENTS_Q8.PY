# Q8.
# Write a Python program to check whether a given key already exists in a dictionary.

# SOLUTION........

n=int(input("enter the number"))
i=1
b={}
while i<=n:
    key=input("enter the key")
    value=input("enter the value")
    b.update({key:value})
    i=i+1
print(b)
user_input=input("enter the input")
if user_input in b:
    print("exists")
else:
    print("not exist")

    
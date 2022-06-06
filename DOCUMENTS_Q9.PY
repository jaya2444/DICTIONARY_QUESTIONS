# Q9.Write a Python program to iterate over dictionaries using for loops.


# SOLUTION..........


n=int(input("enter the number"))
i=1
b={}
while i<=n:
    key=input("enter the key")
    value=input("enter the value")
    b.update({key:value})
    i=i+1
print(b)
for k in b:
    print(k,"=",b[k])

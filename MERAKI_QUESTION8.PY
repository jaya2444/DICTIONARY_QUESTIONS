# Question 8

# Take input of name and marks of 10 students and store to a dictionary.
# Output :-{
#  'sonu':85,
#  'Kartik':90,
#  'Deepak':96,
#  'Aman':76,
#  'Somesh':60,
#  'Umesh':85,
#  'Amarpal':70,
#  'Roshan':57,
#  'Riyaz':98,
#  'Shabid':56
# }

n=int(input("how many elements you want in ur dictionary"))
i=1
a={}
while i<=n:
    name=input("enter the name")
    marks=int(input("enter the marks"))
    i=i+1
    a.update({name:marks})
print(a)




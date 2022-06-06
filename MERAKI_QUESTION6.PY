# Question 6

# Write a program to remove duplicate keys.
# Example :-
# Input :-
# dic={“ball”:”red”,”bat”:4,”wickets”:8,”ball”:green,”bat”:3}
# Output :-
# {“ball”:”red”,”bat”:4,”wickets”:8}


dict1={"ball":"red","bat":4,"wicket":"8","ball":"green","bat":3}
b=[]
a=dict()
for x,y in dict1.items():
    if y not in b:
        b.append(y)
        a[x]=y
print(a)


dict1={"ball":"red","bat":4,"wicket":"8","ball":"green","bat":3}
b={}
for i in dict1:
    if dict1[i] not in b:
        b.update({i:dict1[i]})
print(b)
    




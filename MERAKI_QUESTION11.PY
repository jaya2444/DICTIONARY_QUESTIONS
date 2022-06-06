# Question 11

# Write a program to print the top 3 highest values of a given dictionary.
# Input :-
# my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
# Output :-
# [58,56,100]

my_dict = {'a':50, 'b':58, 'c':56,'d':40, 'e':100, 'f':20}
max=0
b=[]
for x in my_dict:
    if my_dict[x]>max:
        max=my_dict[x]
        max1=0
        for j in my_dict:
            if my_dict[j]>max1 and my_dict[j]!=max:
                max1=my_dict[j]
                max2=0
                for k in my_dict:
                    if my_dict[k]>max2 and my_dict[k]!=max1 and my_dict[k]!=max:
                        max2=my_dict[k]
a=max1,max2,max
b.append(a)
print(b)
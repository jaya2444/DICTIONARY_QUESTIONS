# Question 12

# Write a program to create a dictionary with all numbers from 1 to 15 as the keys and their squares as the corresponding values.
# Output :-
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}


d=dict()
for x in range(1,16):
    d[x]=x**2
print(d)

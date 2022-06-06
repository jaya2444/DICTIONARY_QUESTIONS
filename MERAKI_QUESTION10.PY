# Question 10

# Count the total number of items from the values of the dictionary which are in the form of a list.
# Input :-
# dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# Output :-
# total count:5


dict1 =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
for i in dict1:
    # print(dict1[i])
    c=0
    j=0
    for j in dict1[i][j]:
        c=c+1
print(c)


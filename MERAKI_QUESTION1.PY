# Question 1:-

# Write a program such that the below given dictionaries are into a single dictionary and add the values having same key.
# Example :-
# Input :-
# Code Example
# dic1={1:10, 2:20}
# dic2={3:30,2:40}
# dic3={5:50,6:60}

# Output :-
# {1: 10, 2: 60, 3: 30, 5: 50, 6: 60}


# solution.................

dic1={1:10,2:20}
dic2={3:30,2:40}
dic3={5:50,6:60}
a={}
for i in (dic1,dic2,dic3):
    a.update(i)
for i in a:
    if i in dic1:
        if i in dic2:
            a.update({i:(dic1[i]+dic2[i])})
print(a)
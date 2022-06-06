# Question 4

# Write a program remove the first key value pair from a nested dictionary.
# Example :-
# Input :-
# Dic={1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# Output :-
# Dic= {1: 'NAVGURUKUL',2: 'IN',3:{ 'B' : 'To','C' : 'DHARAMSALA'}}


# SOLUTION BY USING POP METHOD............

# Dic={1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# Dic[3].pop("A")
# print(Dic)

# BY USING DEL METHOD.............

# Dic={1: 'NAVGURUKUL',2: 'IN',  3:{'A' : 'WELCOME','B' : 'To','C' : 'DHARAMSALA'}}
# del Dic[3]["A"]
# print(Dic)
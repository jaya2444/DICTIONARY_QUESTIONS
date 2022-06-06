# Definition :-
# To create a dictionary we put in the key value pairs in a comma separated form inside curly brackets { } and use the colon ":" to assign values to keys`.
# Example:-

# city_population = {
# "NewYorkCity":8550405,
# "LosAngeles":3971883, 
# "Toronto":2731571, 
# "Chicago":2720546, 
# "Houston":2296224, 
# "Montreal":1704694, 
# "Calgary":1239220, 
# "Vancouver":631486, 
# "Boston":667137
# }
# print(city_population["NewYorkCity"])
# print(city_population)
# print(type(city_population))

# Output :-
# 8550405
# {
# "NewYorkCity":8550405,
# "LosAngeles":3971883,
# "Toronto":2731571,
# "Chicago":2720546,
# "Houston":2296224,
# "Montreal":1704694,
# "Calgary":1239220,
# "Vancouver":631486,
# "Boston":667137
# }
#<class 'dict'>

# Keys Case Sensitive :-
# Dictionary keys should be case sensitive, means we can write keys with same names but different case. Python treats them as different keys.
# Example:-
# Dict = {
# 'ball' : 'green',
# 'Ball': 'red'
# }
# print(Dict['ball'])
# print(Dict['Ball'])
# print(Dict['bat'])

# op=
# green
# red
# KeyError: bat
# // KeyError tab aati hai jab key dictionay mai nahi hoti hai.
# In the dictionary, dict , ball a key which has value "green", similarly "Ball" is another key which has value "red".

# dict() function=
# You can create a dictionary using the dict() function.
# Example:-

# student=dict(name= "Ravina",age= 20)
# print(student)

# Output:-
# {'age': 20, 'name': 'Ravina'}

# DataType of Keys and Values:-

# A "dictionary" can have values of any data type and can also be same, but keys are always to be unique.

# Example:-
# dictionary with integer keys:-
# Code Example
# my_dict = {
# 1: 'apple', 
# 2: 'ball'
# }

# dictionary with mixed keys:-
# Code Example
# my_dict = {
# 'name': 'John',
#  1: [2, 4, 3]
# }


# Nested Dictionary :-
# Code Example

# Dic= {
# 1: 'NAVGURUKUL',
# 2: 'IN',  
# 3:{
# 'A' : 'WELCOME',
# 'B' : 'To', 
# 'C' : 'DHARAMSALA'
# }
# }
# print(Dic)

# Output :-
# {1: 'NAVGURUKUL', 2: 'IN', 3: {'A': 'WELCOME', 'B': 'To', 'C': 'DHARAMSALA'}}


# Accessing Elements from a Dictionary:-

# We can access dictionary values with the use of square brackets. Look at the example below to understand.
# Example :-

# person={
# 'name':'jack',
# 'age':20,
# 'gender':'male',
# 4:'organisation'}
# result = person['age'] 
# x = person.get("gender")
# print(person[4])
# print(x)
# print(result)

# Output :-
# organisation male 20


# get() :-

# We can also make use of the get() function to access dictionary values.
# Example :-

# person={
# 'name':'jack',
# 'age':20,
# 'gender':'male',
# 4:{
# 'organisation':'navgurukul','place':'dharamsala'
# }
# }
# print(person['gender'])
# print(person[4])
# result = person[4]['place']
# print(result)

# Output :-
# male
# {'organisation': 'navgurukul', 'place': 'dharamsala'}
# dharamsala


# Adding Elements to a Dictionary:-

# In a python dictionary we can add only one key value pair at a time. To add to a dictionary we mention the key inside square brackets "[ ]" and use the equal to "=" operator to assign a value.
# Example :-

# dic= {
# 'Name': 'RAM', 
# 'Age': 17,
# }
# dic['ORGANIZATION'] = "NAV GURUKUL"
# dic['place'] = 'dharamsala'
# print(dic)

# Output :-
# {'Name': 'RAM', 'Age': 17,'ORGANIZATION': 'NAVGURUKUL', 'place':'dharamsala}


# Example :-

# dic= {
# 'Name': 'RAM',
# 'Age': 17,
# }
# dic['student']={
# 'id':22, 
# 'place':'dharamsala'
# }
# print(dic)

# Output:-
# {'Name': 'RAM', 'Age': 17, 'student': {'id': 22, 'place': 'dharamsala'}}



# Key Exists or not:-

# We use the in keyword to check whether a given key exists or not in a dictionary.
# Code Example

# car ={
# "brand":  "ford",
# "model":  "mustang",
# "year":  1964
# }
# if "model" in car:
#     print("Yes, 'model' is one of the keys in the car dictionary.")
# else:
#     print("No, 'model' key dictionary mai nahi hai.")

# Output :-
# Yes, 'model' is one of the keys in the this dict dictionary

# Updating Dictionary :-

# To update dictionary ,we can make an entry in it or we can add a key-value pair or we can change the value of an existing key. As given in the example explained:-
# Example 1:-

# person= {'1': 'RAM', '2': 17,}
# person[3] = 'male'
# print(person)

# Output:-
# {'1': 'RAM', '2': 17,'3':'male'}

# Example 2 :-

# details={
# 'Name': 'RAM',
# 'Age': 17, 
# 'student': {
# 'id': 22,
# 'place': 'dharamsala'
# }
# } 
# details['student']['id']=35
# print(details);

# Output:-
# {'Name': 'RAM', 'Age': 17, 'student': {'id': 35, 'place': 'dharamsala'}}


# Copy of Dictionary :-

# We can copy a dictionary in two ways,first method is using copy() and second method by using built-in function dict().
# Example 1 :-

# classes ={
# "room1":  "6th",
# "room2":  "7th",
# "room3":  "8th"
# }
# mydict=classes.copy()
# print(mydict)

# Output :-
# {'room2': '7th', 'room3': '8th', 'room1': '6th'}

# Removing Elements from a Dictionary:-

# We can remove dictionary elements by many methods.
# Like given below.
# pop() :-
# Using the pop( ) method we can remove a specified element from the dictionary.
# Code Example:-

# CAR_DETAILS={
# "brand": "Ford",
# "model": "jason",
# "year": 1964
# }
# CAR_DETAILS.pop("model")
# print(CAR_DETAILS)

# Output:-
# {'brand': 'Ford', 'year': 1964}

# popitem():-

# The popitem() method removes the last inserted item:
# Code Example:-

# person={
# 'name':'jack',
# 'id':22,
# 'place':'dharamsala'
# }
# person.popitem()
# print(person)

# Output:-
# {'name':'jack','id':22}

# del :-
# Using the del keyword we can remove a specified element from the dictionary.
# Code Example:-

# person={
# 'name':'jack',
# 'id':22,
# 'place':'dharamsala'
# }
# del person('place')
# print(person)

# Output:-
# {'name':'jack','id':22}

# iterations:-
# Iterate through all keys:-
# Code Example:-

# states_capitals = {
# 'Gujarat' : 'Gandhinagar',
# 'Maharashtra' : 'Mumbai',
# 'Rajasthan' : 'Jaipur',
# 'Bihar' : 'Patna'
# }
# for state in states_capitals:
#   print(state)

# Output:-
# Gujarat Maharashtra Rajasthan Bihar

# Iterate through all values:-
# Example :-

# states_capitals = {
# 'Gujarat' : 'Gandhinagar',
# 'Maharashtra' : 'Mumbai',
# 'Rajasthan' : 'Jaipur',
# 'Bihar' : 'Patna'
# }
# for state in states_capitals:
#     print(states_capitals[state])

# Output :-
# Gandhinagar<br> Mumbai<br> Jaipur<br> Patna

# Example :-

# details ={
# "name":  "Bijender",
# "age":  17,
# "class":  "10th"
# }
# for x in details.values():
#     print(x)

# Output :-
# 17<br>Bijender<br>10th<br>

# Example :-
# How to print keys and values together from a dictionary?

# movie ={
# "name":  "Puli",
# "hero":  "Vijay",
# "rating":  7.5
# }
# for x,y in movie.items():
#     print(x,y)

# Output :-
# ('rating', 7.5)<br>('hero', 'Vijay')<br>('name', 'Puli')<br>

# Dictionary length:-

# We use Dictionary length to find the number of items/key value pairs in a dictionary.
# Example:-

# meal ={
# "monday":  "Chole chawal",
# "sunday":  "Fried rice",
# "wednesday":  "dosa"
# }
# print(len(meal))

# Output :-
# 3




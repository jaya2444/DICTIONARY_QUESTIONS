# Q7.
# Write a Python script to concatenate the following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

# SOLUTION...............

dic1={1:10,2:20}
dic2={3:30,4:40}
dic3={5:50,6:60}
a={}
for i in (dic1,dic2,dic3):
    a.update(i)
for i in a:
    if i in dic1:
        if i in dic2:
            a.update({i:(dic1[i]+dic2[i])})
print(a)
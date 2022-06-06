# question7

# Take a list having dictionary elements as shown below (Sample Data) and then store all the unique values into a list and print.
# Example :-
# Input :-
# [{"first":"1"}, {"second": "2"}, {"third": "1"}, {"four": "5"}, {"five":"5"},{"six":"9"},{"seven":"7"}]
# Output :-
# ['2', '7', '9', '5', '1']

# L =[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
# print("Original List: ",L)
# u_value = set( val for dic in L for val in dic.values())
# print("Unique Values: ",u_value)

# L =[{"first":"1"},{"second": "2"},{"third": "1"},{"four": "5"},{"five":"5"},{"six":"9"},{"seven":"7"}]
# b=[]
# for i in range(len(L)):
#     for j in L[i].values():
#         if j not in b:
#             b.append(j)
# print(b)


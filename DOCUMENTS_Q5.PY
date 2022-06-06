# Q5.
# Write a Python program to sort (ascending and descending) a dictionary by value.
# Original dictionary : {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# Dictionary in ascending order by value : [(0, 0), (2, 1), (1, 2), (4, 3), (3, 4)]
# Dictionary in descending order by value : {3: 4, 4: 3, 1: 2, 2: 1, 0: 0}

# SOLUTION...........


# dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# a=[]
# c={}
# for i in dic:
#     a.append(dic[i])
# # print(a)    
# for j in range(len(a)):
#     for k in range(len(a)-1):
#         if a[k]>a[k+1]:
#             t=a[k]
#             a[k]=a[k+1]
#             a[k+1]=t
# # print(a)           
# for m in range(len(a)):
#       for l in dic:
#           if dic[l]==a[m]:
#               c.update({l:(dic[l])})
# print(c)

# SECOND SOLUTION.......

# dic={1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
# a=[]
# c={}
# for i in dic:
#     a.append(dic[i])
# # print(a)    
# for j in range(len(a)):
#     for k in range(len(a)-1):
#         if a[k]<a[k+1]:
#             t=a[k]
#             a[k]=a[k+1]
#             a[k+1]=t
# # print(a)           
# for m in range(len(a)):
#       for l in dic:
#           if dic[l]==a[m]:
#               c.update({l:(dic[l])})
# print(c)

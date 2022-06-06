# Question 14
# Write a program to sort a dictionary in ascending or descending according to its values .
# Input :-
# {'bijender':45,'deepak':60,'param':20,';'anjili':30,'roshini':50}
# Expected result in Ascending Order:
# {'param':20,'anjili':30,'bijender':45,'roshini':50,'deepak':60}
# Expected result in Descending Order:
# {'deepak':60,'roshini':50,'bijender':45,'anjili':30,'param':20}

#  DICTIONARY IN ascending ORDER(keys).................

# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# print("original dictionary",a)
# b={}
# b.update(sorted(a.items()))
# print("ascending order",b)


#DICTIONARY IN DESENDING ORDER(keys).........

# a={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# print("original dictionary",a)
# b={}
# b.update(sorted(a.items(),reverse=True))
# print("desending order",b)


#  DICTIONARY IN ascending ORDER(values).................

# dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
# a=[]
# c={}
# for i in dic:
#     a.append(dic[i])
# print(a)    
# for j in range(len(a)):
#     for k in range(len(a)-1):
#         if a[k]>a[k+1]:
#             t=a[k]
#             a[k]=a[k+1]
#             a[k+1]=t
# print(a)           
# for m in range(len(a)):
#       for l in dic:
#           if dic[l]==a[m]:
#               c.update({l:(dic[l])})
# print(c)

#  DICTIONARY IN desending ORDER(values).................

dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
a=[]
c={}
for i in dic:
    a.append(dic[i])
print(a)    
for j in range(len(a)):
    for k in range(len(a)-1):
        if a[k]<a[k+1]:
            t=a[k]
            a[k]=a[k+1]
            a[k+1]=t
print(a)           
for m in range(len(a)):
      for l in dic:
          if dic[l]==a[m]:
              c.update({l:(dic[l])})
print(c)



# question3

# Ek program likhiye jo ki dictionaries ki values ka sum print kare.
# Example :-
# Input :-
# Code Example

# my_dict = {
# 'data1':100,
# 'data2': -54,
# 'data3': 247
# }
# Output :-
# 293

# SOLUTION................

my_dict = {'data1':100,'data2': -54,'data3': 247}
sum=0
for x in my_dict:
    sum=sum+my_dict[x]
print(sum)
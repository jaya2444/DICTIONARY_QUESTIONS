# Question 9

# Store the unique letters and their frequency of the letters from the word "MISSISSIPPI" to a dictionary, were the letters are the keys and their frequencies are the values.
# Example:-
# Output :-
# {'M':1,'I':4,'S':4,'P':2}


l="MISSISSIPPI"
# l='brontosaurus' 
a=(sorted(list(l)))
i=0
count=0
b=[]
while i<len(a):
        j=0
        b1=[]
        count=0
        while j<len(a):
                if a[i] in a:
                        if a[i]==a[j]:
                                count+=1
                        j+=1
        b1.append(a[i])
        b1.append(count)
        if b1 not in a:
                b.append(b1)
        i+=1
print(dict(b))


str1 = "MISSISSIPPI"
my_dict = {}
for letter in str1:
    my_dict[letter] = my_dict.get(letter, 0) + 1
print(my_dict)
# Q2. Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, '
dic={}
string = input("enter the string: ")
i=0
while i<len(string):
    j=0
    count=0
    while j<len(string):
        if string[j]==string[i]:
            count=count+1
            dic.update({string[i]:count})
        j=j+1
    i=i+1
print(dic)
    
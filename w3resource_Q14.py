#Q 16. Write a Python program to get a dictionary from an object's fields. 

list1=["a","b","c","d"]
list2=[1,2,3,4,]
dic={}
i=0
while i<len(list1):
    dic.update({list1[i]:list2[i]})
    i=i+1
print(dic)


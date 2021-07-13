list1=["one","two","three","four","five"]
list2=[1,2,3,4,5,]
new_dict={}
i=0
while i<len(list2):
    new_dict[list1[i]]=list2[i]
    i=i+1
print(new_dict)
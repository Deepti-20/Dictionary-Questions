dic={'bijender':45,'deepak':60,'param':20,'anjili':30,'roshini':50}
key_list=[]
value_list=[]
for key in dic:
    key_list.append(key)
    value_list.append(dic[key])


for key1 in range(0,len(key_list)):
    for value in range(0,len(key_list)):
        if value_list[key1]<value_list[value]:
            value_list[key1],value_list[value]=value_list[value],value_list[key1]
            key_list[key1],key_list[value]=key_list[value],key_list[key1]

dic={}
for index in range(0,len(key_list)):
    dic[key_list[index]]=value_list[index]
print(dic)

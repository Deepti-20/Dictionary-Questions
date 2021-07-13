key=['apple','mango','grape','banana','blackberry']
value=['red','yellow','green','yellow','black']
dic={}
i=0
while i<len(key):
    dic.update({key[i]:value[i]})
    i=i+1
print(dic)


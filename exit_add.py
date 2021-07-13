
dic={'a': 400, 'b': 400, 'd': 400, 'c': 300}
user=input("enter the element---")
for i in dic:
    if i==user:
        print("this key already exist....")
        break
else:
    value1=input("enter any value...")
    dic.update({user:value1})
    print(dic)
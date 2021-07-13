i=1
dic={}
while i<=10:
    user1=input("enter keys...")
    user2=int(input("enter value..."))
    j=0
    while j<user2:
        dic.update({user1:user2})
        j=j+1
    i=i+1
print(dic)



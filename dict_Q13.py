my_dict = {'a':50,'b':58,'c': 56,'d':40,'e':100,'f':20}
max=0
list=[]
for x,y in my_dict.items():
    if y>max:
        max=y
        key=x  
        sec=0
        for j,k in my_dict.items():
            if max>k>sec:
                sec=k
                key1=j
                third=0
                for m,n in my_dict.items():
                    if max>sec>n>third:
                        third=n
                        key2=m
list.append(key)
list.append(key1)
list.append(key2)
print(list)                      
print(max,key)
print(sec,key1)
print(third,key2)


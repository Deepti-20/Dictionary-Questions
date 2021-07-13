dic1 = {'a': 100, 'b': 200, 'c':300}
dic2 = {'a': 300, 'b': 200, 'd':400}
total_dic={}
for x in dic1:
    for y in dic2:
        if x == y:
            add = dic1[x]+dic2[y]
        else:
            total_dic[x] = dic1[x]
            total_dic[y] = dic2[y]
    
    total_dic["a"]=add
total_dic["b"]=add
  
print(total_dic)

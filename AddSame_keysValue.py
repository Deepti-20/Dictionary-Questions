# Q19. Write a Python program to combine two dictionary adding values for common keys. 
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

dic1 = {'a': 100, 'b': 200, 'c':300}
dic2 = {'d': 300, 'c': 200, 'a':400}
total_dic={}
for i in dic1:
    for j in dic2:
        if i == j:
            total_dic[i] = dic1[i]+dic2[j]
            break
    else:
        total_dic[i] = dic1[i]
        total_dic[j] = dic2[j]
print(total_dic)



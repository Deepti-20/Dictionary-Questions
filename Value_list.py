# 21. Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:ac  ad  bc  bd

dic={'1':['a','b'], '2':['c','d']}
for x in dic:
    i=0
    while i<len(dic[x]):
        j=1
        while j<len(dic[x]):
            print(dic[x][j])
            #print(dic[x][i]+dic[x][j])
            j=j+1
        i=i+1
    break


# dic={'1':['a','b'], '2':['c','d']}
# lis=[]
# for x in dic:
#     lis.append(x)
#     #print(lis)
#     i=0
#     while i<len(lis[lis]):
#         j=0
#         while j<len(dic[lis]):
#             print(lis[1][i]+lis[2][j])
#             j=j+1
#         i=i+1

    




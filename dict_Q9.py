string="MISSISSIPPI"
i=0
dic={}
while i<len(string):
    j=0
    count=0
    while j<len(string):
        if string[i]==string[j]:
            count=count+1
        dic.update({string[i]:count})
        j=j+1
    i=i+1
print(dic)


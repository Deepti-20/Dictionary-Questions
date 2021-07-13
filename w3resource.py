# 20. Write a Python program to print all unique values in a dictionary. Go to the editor
# Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, 
# {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}


Sample_Data =[{"V":"S001"},{"V":"S002"},{"VI":"S001"},{"VI":"S005"},{"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
#print(Sample_Data)
lis=[]
dic={}
for x in Sample_Data:
    for i in x:
        if x[i] not in lis:
            lis.append(x[i])

print(lis)

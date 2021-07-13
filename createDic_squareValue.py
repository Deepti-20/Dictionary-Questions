# .Write a Python script to generate and print a dictionary that contains a number (between 1 and n) in the form (x, x*x).
# Sample input ( n = 5) :
# Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}.


num=int(input("enter any number.."))
dic={}
i=1
while i<=num:
    dic.update({i:i*i})
    i=i+1
print(dic)
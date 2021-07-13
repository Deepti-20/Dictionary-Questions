# Ek dictionary me 1 se 15 tak saare numbers ki keys banaye aur unke square unn
#  keys ki values ho. Output :-
dic={}
i=1
while i<=15:
    square=i*i
    dic.update({i:square})
    i=i+1
print(dic)


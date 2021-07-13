my_dict = {'a':50,'b':58,'c':56,'d':40,'e':100,'f':20}
max=0
for i in my_dict.values():
    if i>max:
        max=i
        sec_max=0
        for j in my_dict.values():
            if max>j>sec_max:
                sec_max=j
                third_max=0
                for k in my_dict.values():
                    if max>sec_max>k>third_max:
                        third_max=k
print(third_max)
print(sec_max)
print(max)


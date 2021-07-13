user=input("enter input:--> ")
dict1={"name":"raju","marks":56}
for user in dict1.keys():
    if user in dict1.keys():
        print("exist")
        break
    elif user not in dict1.keys():
        print("not exist")
        break



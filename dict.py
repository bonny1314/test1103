# account = {"username":"huang","passw":"1234"}
# for a in account: 
#     print(a)             #get key
#     print(account[a])    #get value



account=[{"username":"huang","password":"1234"},{"username":"zhang","password":"1234"}]
time=1
username=input("input your name: ")
password=input("input your password:")
for u in account:
    print("the {} times run======".format(time))
    if u["username"] == username:
        print("the username has existed")
        break  # exit run
    else:
        if time == len(account):  
           user = {"username":username,"password":password}  ##ident gen time duiqi  zhuyi suojin
           account.append(user)                              ##ident gen time duiqi  zhuyi suojin
           print("user has registed")
           break
    time=time+1
        
print(account)



### kankan zhanghao shifou cunzai  bucunzai jiu zhuce
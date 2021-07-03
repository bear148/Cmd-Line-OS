import home as H
import os
import rootTerminal as RT
import time

login_pass = open('data/password.pass')
login_name = open('data/username.pass')
l_p = login_pass.read()
l_n = login_name.read()

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def devTermMain():
    os.system('clear')
    print("Welcome to the Bear OS Terminal")
    print("Ver 1.2.4")
    print("(DEVELOPER MODE: ACTIVATED) (ROOT: TRUE)")
    def helpCom():
        os.system('clear')
        print("""
        Exit: Returns you to menu
        UserInfo: Tells you current user's information
        Root: Allows root terminal access
        python3: Allows you to run .py files
        clear: Clears screen

        More commands to come with future updates:
        """)

    while True:
        bruhVariable = input(f"{bcolors.OKBLUE}Bear OS >>{bcolors.OKGREEN} ")

        pyfile = bruhVariable.endswith(".py")

        m = str(pyfile)

        if bruhVariable == "Help":
            os.system('clear')
            helpCom()
        elif bruhVariable == "help":
            os.system('clear')
            helpCom()

        elif bruhVariable == "Exit":
            os.system('clear')
            H.devPage()
            break
        elif bruhVariable == "exit":
            os.system('clear')
            H.devPage()
            break

        elif bruhVariable == "UserInfo":
            os.system('clear')
            print("Username: " + l_n)
            print("Password: " + l_p)

        elif bruhVariable == "userinfo":
            os.system('clear')
            print("Username: " + l_n)
            print("Password: " + l_p)

        elif bruhVariable == "clear":
            os.system('clear')

        elif bruhVariable == "Clear":
            os.system('clear')
        
        elif bruhVariable == "python3":
            m = input("What file would you like to run? ")
            if m.endswith('.py'):
                os.system(f'python3 {m}')
            else:
                print(m + " is not a py file.")

        elif bruhVariable == "restart":
            print("Restarting...")
            time.sleep(1)
            exec(open('BearCMDos.py').read())

        else:
            print("The command, " "" + bruhVariable + "" " wasn't found!")
import requests as r
import re
import getpass

def b():
    print("="*60)

def carryon(url):
    login_data = {'username': username, 'password': password}
    log = r.post(url, data=login_data)
    return log.text

def log_in(url):
    if username == "":
        print("you did not add a username")
        print("-"*60)
        sure = input("do you want to continue like that y/n: ")
        if sure == 'y':
            return url
        elif sure == 'n':
            exit()
        else:
            print("y/n nah I no too sabi program")
    else:
        return url

def check_login(login_text):
    correct_pattern = re.compile(r"You are (\w+)")
    wrong_pattern = re.compile(r"invalid username or (\w+)")
    try:
        valid = re.search(correct_pattern, login_text).group(1)
    except:
        valid = re.search(wrong_pattern, login_text).group(1)
    if valid == "logged":
        b()
        print("\nyou are logged in\n")
        b()
        b()
        print("Your remaining bytes is ",pull_quota("http://172.16.2.254/status"))
        b()
        return 0
    elif valid == "already":
        b()
        print("\nyou are already logged in")
        b()
    elif valid == "password":
        b()
        print("\ninvalid username or password")
        b()
    else:
        b()
        print("\nYou are not logged in")
        b()

def pull_quota(statuspage):
    get_quota = r.get(statuspage).text
    pattern = re.compile(r"readablizeBytes\((\d+)")
    readablizeBytes = re.search(pattern , get_quota).group(1)
    print(sizeof_fmt(int(readablizeBytes)))
    return readablizeBytes

def logout(url):
    r.get(url)
    print("You have been logged out")

def sizeof_fmt(num, suffix='B'):
    for unit in ['','Ki','Mi','Gi','Ti','Pi','Ei','Zi']:
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, 'Yi', suffix)

b()
tree = int(input('''
1.) Login
2.) Logout
3.) Status \n:--> '''))
b()

if tree == 1:
    print(".*"*30)
    print("-"*60)
    username = input("username:--> ")
    print("-"*60)
    password = getpass.getpass("Enter Password:--> ")
    check_login(carryon(log_in('http://172.16.2.254/login')))
elif tree == 2:
    logout("http://172.16.2.254/logout")
elif tree == 3:
    print("your remaininig quota is: ")
    print(pull_quota('http://172.16.2.254/status'))
    b()
else:
    b()
    print("Nigga 1 or 2!!!")
    b()
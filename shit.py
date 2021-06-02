import requests as r
import re
import getpass
import json

# public assignments
username = input("username:--> ")
password = getpass.getpass("Enter Password:--> ")

#######################################################
#####                 My Exceptions               #####
class Error(Exception):
    """Base class for other exceptions"""
    pass
class AlreadyLoggedin(Error):
    """Raised when you are already logged in"""
    pass
class InvalidDetails(Error):
    """Raised when you give invalid details"""
    pass
#########################################################

def log_in(url):
    login_data = {'username': username, 'password': password}
    log = r.post(url, data=login_data)
    # print(log.text)
    return log.text

def check_login(login_text):
    # print(login_text)
    correct_pattern = re.compile("You are logged (\w+)")
    logged_pattern = re.compile("You are already (\w+)")
    wrong_pattern = re.compile("invalid username or (\w+)")
    try:
        valid = re.search(correct_pattern, login_text).group(1)
        if valid == "in":
            print("\nyou are logged in")
            status = "http://internetlogin1.cu.edu.ng/status"
            return status               
        else:
            raise AlreadyLoggedin
    except AlreadyLoggedin:
        valid = re.search(logged_pattern, login_text).group(1)
        if valid == "logged":
            print("\nyou are already logged in")
        else:
            raise InvalidDetails
    except InvalidDetails:
        try:
            valid = re.search(wrong_pattern, login_text).group(1)
            if valid == "password":
                print("\ninvalid username or password")
            else:
                print("\nConnection Issues")
        except:
            print("\nConnection Issues")
    # except:
    #     print("confused")
    #     raise InvalidDetails

def pull_quota(statuspage):
    get_quota = r.get(statuspage).text
    pattern = re.compile("readablizeBytes\((\d+)")
    readablizeBytes = re.search(pattern , get_quota).group(1)
    quota = readablizeBytes.replace('readablizeBytes\(', '')
    # print(quota)
    return quota


# print(pull_quota("http://internetlogin1.cu.edu.ng/status"))
check_login(log_in('http://172.16.2.254/login'))
# dst=&popup=true&username=fake&password=fake
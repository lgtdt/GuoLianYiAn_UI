import hashlib
import subprocess
import  datetime
import os
from db.password_policy_Function import Get_Password_Policy

def md5_encrypt(input):
    md5_obj = hashlib.md5()
    md5_obj.update(input.encode('utf-8'))
    encrypted_string = md5_obj.hexdigest()
    return encrypted_string
def if_Passwd_Right(inputPasswd, truePasswd):
    if inputPasswd == truePasswd:
        return True
    else:
        return False
def GetTimeFromTimeStamp(time_stamp):
    dt_object = datetime.datetime.fromtimestamp(time_stamp)
    year = dt_object.year
    month = dt_object.month
    day = dt_object.day
    hour = dt_object.hour
    minute = dt_object.minute
    second = dt_object.second
    result = f"{year}-{month:02d}-{day:02d}-{hour:02d}:{minute:02d}:{second:02d}"
    return result

def CheckConfig():
    if not os.path.exists('./config.ini'):
        return "Could not find the config file.Please check."
    else:
        return "success"
def CheckPass(password):
    pass_policy = Get_Password_Policy()
    upper_num = pass_policy[0]
    lower_num = pass_policy[1]
    symbol_num = pass_policy[2]
    digit_num = pass_policy[3]
    min_len_num = pass_policy[4]

    upper, lower, symbol, digit, len = 0, 0, 0, 0, 0
    special_characters = "!@#$%^&*()_+-=[]{}|;:'\",.<>?`~"
    for char in password:
        if char.isupper():
            upper += 1
        if char.islower():
            lower += 1
        if char.isdigit():
            digit += 1
        if char in special_characters:
            symbol += 1
        len += 1
    if(upper >= upper_num and lower >= lower_num and symbol >= symbol_num and digit >= digit_num and len >= min_len_num):
        return True
    else:
        return False


def execute_Command_Realtime(command):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, shell=True, text=True)
        while True:
            line = process.stdout.readline()
            if line == '' and process.poll() is not None:
                return "Done"
                break
            return line.strip()
    except Exception as e:
        return str(e)
def File_in_Path(path):
    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            return file_path

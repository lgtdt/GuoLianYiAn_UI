import hashlib

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
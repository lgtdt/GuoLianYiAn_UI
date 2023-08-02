import hashlib

def md5_encrypt(input):
    md5_obj = hashlib.md5()
    md5_obj.update(input.encode('utf-8'))
    encrypted_string = md5_obj.hexdigest()
    return encrypted_string
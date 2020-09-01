# модуль для шифрования и дешифровки json при общении с базой данных
import rsa
from settings import pubkey_pem, privkey_pem


pubkey = rsa.PublicKey.load_pkcs1(pubkey_pem, 'PEM')
privkey = rsa.PrivateKey.load_pkcs1(privkey_pem, 'PEM')


def encrypt_all(data_list):
    encrypt_list = []
    if type(data_list) == str:
        encrypt_element = encrypt_point(data_list)
        encrypt_list.append(encrypt_element)
    else:
        for data in data_list:
            encrypt_element = encrypt_dict(data)
            encrypt_list.append(encrypt_element)
    return encrypt_list


def encrypt_dict(dictionary: dict):
    encrypted_dict = {}
    for key, value in dictionary.items():
        if key == 'data':
            encrypted_dict[key] = encrypt_dict(value)
        elif key == '_id' or key == 'chat_id':
            encrypted_dict[key] = value
        else:
            encrypted_dict[key] = rsa.encrypt(str(value).encode('utf8'), pubkey)
    return encrypted_dict


def encrypt_point(point):
    encrypted_point = rsa.encrypt(point.encode('utf8'), pubkey)
    return encrypted_point


def decrypt_all(data_list) -> list:
    decrypt_list = []
    if type(data_list) == str:
        decrypt_element = decrypt_point(data_list)
        decrypt_list.append(decrypt_element)
    else:
        for data in data_list:
            decrypt_element = decrypt_dict(data)
            decrypt_list.append(decrypt_element)
    return decrypt_list


def decrypt_dict(dictionary: dict):
    decrypted_dict = {}
    for key, value in dictionary.items():
        if key == 'data':
            decrypted_dict[key] = decrypt_dict(value)
        elif key == '_id' or key == 'chat_id':
            decrypted_dict[key] = value
        else:
            item = rsa.decrypt(value, privkey)
            decrypted_dict[key] = item.decode('utf8')
    return decrypted_dict


def decrypt_point(point):
    item = rsa.decrypt(point, privkey)
    decrypted_point = item.decode('utf8')
    return decrypted_point





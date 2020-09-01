import rsa
from settings import pubkey_pem, privkey_pem

pubkey = rsa.PublicKey.load_pkcs1(pubkey_pem, 'PEM')
privkey = rsa.PrivateKey.load_pkcs1(privkey_pem, 'PEM')


def encrypt_dict(dictionary: dict):
    encrypted_dict = {}
    for key, value in dictionary.items():
        if key == 'data': 
            encrypted_dict[key] = encrypt_dict(value)
        elif key == 'chat_id': encrypted_dict[key] = value
        else:
            encrypted_dict[key] = rsa.encrypt(str(value).encode('utf8'), pubkey)
    return encrypted_dict


def decrypt_dict(dictionary: dict):
    decrypted_dict = {}
    for key, value in dictionary.items():
        if key == 'data':
            decrypted_dict[key] = decrypt_dict(value)
        elif key == '_id' or key == 'chat_id': continue
        else:
            item = rsa.decrypt(value, privkey)
            decrypted_dict[key] = item.decode('utf8')
    return decrypted_dict

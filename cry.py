import os
from cryptography.fernet import Fernet

def generate_key_file(path="."):
    key=Fernet.generate_key()
    with open(path+"/key.key", "wb") as key_file:
        key_file.write(key)

def encrypt_file(filename, key=None, key_filename=None):
    if key is None and key_filename is None:
        raise TypeError("You muse specify a key or a keyfile.")
    
    if key_filename:
        with open(key_filename, "rb") as kfi:
            key = kfi.read()

    with open(filename, "rb") as fi:
        content = fi.read()
    encrypted_content = Fernet(key).encrypt(content)
    
    with open(filename, "wb") as fo:
        fo.write(encrypted_content)


def decrypt_file(filename, key=None, key_filename=None):
    if key is None and key_filename is None:
        raise TypeError("You muse specify a key or a keyfile.")
    
    if key_filename:
        with open(key_filename, "rb") as kfi:
            key = kfi.read()

    with open(filename, "rb") as fi:
        encrypted_content = fi.read()
    
    decrypted_content = Fernet(key).decrypt(encrypted_content)

    with open(filename, "wb") as fo:
        fo.write(decrypted_content)
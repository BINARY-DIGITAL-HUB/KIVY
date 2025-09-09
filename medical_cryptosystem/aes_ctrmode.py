import base64
from ctypes import sizeof
from Crypto.Cipher import AES
from numpy import byte 
import time

data = b'ade-12-yes-1995'

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ctr-

# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html

import json
from base64 import b64encode
from Crypto.Cipher import AES
from Crypto.Util import Counter
from Crypto.Random import get_random_bytes
from pathlib import Path
import json
from base64 import b64decode
from Crypto.Cipher import AES
import csv as cv
import rsa_encryption as rsa
from binascii import hexlify, unhexlify


class AESCTRXEncryption:

    def __init__(self) -> None:
        self.key = None

        # generate and RSA key for each encryption 
        self.rsa = rsa.RSAEncryption()
        self.private , self.public = ('', '')


    def encrypt(self, plain_text, id , passcode):

        # GENERATING RSA KEY
        self.rsa.generateKeys()

        self.private , self.public = self.rsa.loadKeys()   # retrurn a turple of private, public key


        # data = b"secret"
        data =  bytes(plain_text, 'utf-8')
        # self.key = get_random_bytes(16)

        # counter =  Counter.new(nbits=16, prefix= unhexlify('f0f1f2f3f4f5f6f7f8f9fafbfcfd'), initial_value=0xfeff)

        self.key = bytes(passcode, 'utf-8')
        # print("KEY SIZE" , len(self.key))
        cipher = AES.new(self.key, AES.MODE_CTR)

        
        start_time = time.time()
        
        ct_bytes = cipher.encrypt(data)
        nonce = b64encode(cipher.nonce).decode('utf-8')
        
        # ENCRYPT  the PASSCODE before placed in the BINARY FILE
        # USING THE RSA ALGORITHM......
        passcode = self.rsa.encrypt(passcode , self.public)
        end_time = time.time()

        # print('Encryption Time ', (end_time-start_time)*1000)
        # print('decrypted ', passcode)
        pk_file = open(str(id), 'wb')
        pk_file.write(passcode)
        pk_file.close()

        
        
        # passcode = base64.b64encode(passcode)
        # print(passcode)

        # self.cerfertext = self.encrypt(self.key, self.public)
        ct = b64encode(ct_bytes).decode('utf-8')
        result = json.dumps({'nonce':nonce, 'ciphertext':ct})
        Path(str(id)+".json").write_text(result)

        # print(result)
        return (end_time-start_time)*1000


    def decrypt(self, id_file , passcode):
         # We assume that the key was securely shared beforehand
        data = Path(str(id_file)+'.json').read_text()
        try:
            b64 = json.loads(data)
            nonce = b64decode(b64['nonce'])
            ct = b64decode(b64['ciphertext'])
            # key_text = b64['Code']

            # decrypting the AES KEY  with RSA encryption 
            # key_text = key_text.decode("ascii")
            # rsa_key_decrypt = self.r.decrypt(self.key , self.private)
            
            self.private , self.public = self.rsa.loadKeys()  
             # retrurn a turple of private, public key


        # DECRYPT  the CTR KEY.. LOAD BINARY FILE.. 
        # USING THE RSA ALGORITHM......
            pk_read = open(str(id_file), 'rb')
            pass_key = pk_read.read()
            pk_read.close() 
            # print('AES KEY SIZE ' , len(pass_key))
            # print(f'RSA key SIZE private:{sizeof(self.private)}  public:{sizeof(self.public)}')
            start_time2 = time.time()
            pass_key = self.rsa.decrypt(pass_key, self.private)
            # print('decrypted ', pass_key)
            # temp key movement
            self.key = bytes(pass_key, 'utf-8')

            # key = bytes(rsa_key_decrypt, 'utf-8')
            cipher = AES.new(self.key, AES.MODE_CTR, nonce=nonce)
            pt = cipher.decrypt(ct)
            end_time2 = time.time()
            # print("The message was: ", pt)
            return pt , (end_time2-start_time2)*1000
        except (ValueError, KeyError):
            print("Incorrect decryption")

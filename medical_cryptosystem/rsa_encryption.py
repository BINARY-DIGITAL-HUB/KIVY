
import rsa

class RSAEncryption():

    def generateKeys(self):
        (publicKey, privateKey) = rsa.newkeys(1024)
        with open('keys/publicKey.pem', 'wb') as p:
            p.write(publicKey.save_pkcs1('PEM'))
        with open('keys/privateKey.pem', 'wb') as p:
            p.write(privateKey.save_pkcs1('PEM'))

    def loadKeys(self):
        with open('keys/publicKey.pem', 'rb') as p:
            publicKey = rsa.PublicKey.load_pkcs1(p.read())
        with open('keys/privateKey.pem', 'rb') as p:
            privateKey = rsa.PrivateKey.load_pkcs1(p.read())
        return privateKey, publicKey

    def encrypt(self, message, key):
        return rsa.encrypt(message.encode('ascii'), key)

    
    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False
    
    def decrypt(self, ciphertext, key):
        try:
            return rsa.decrypt(ciphertext, key).decode('ascii')
        except:
            return False



# rs = RSAEncryption()
# # rs.generateKeys()

# private, public = rs.loadKeys()
# print(f'private {private} \n public {public}')

# cipher_text = rs.encrypt('1995' , public)
# print('message encrypted succesfully')

# message = rs.decrypt(cipher_text, private)
# print(f'original_message {message}')
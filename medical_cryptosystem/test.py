import time as time
from datetime import datetime
import sys

from aes_ctrmode import AESCTRXEncryption




crypo = AESCTRXEncryption()
# this is a comment update


data = "0-Robyn-30-female-yes-no-1.0-1.0"
size = sys.getsizeof(data)
print(f'DATA SIZE OF ONE RECORD === > , {size/1000} KB')
print(f'DATA SIZE FOR ENTIRE DATABASE  === > , {(size/1000)*155} KB')
print('\nENCRYPTION TIME FOR THE PROPOSED RSA AND COUNTER CTR')
start_time = time.time()

encryp_time = crypo.encrypt(data , 5 , '1234567891234567')   
end_time = time.time()
# encryp_time = (end_time-start_time)*1000
print(f'Encryption Time (one record (0.081KB))========>, {encryp_time} (ms)')
print(f'Encryption Time (ALL record (12KB))========>, {encryp_time*155} (ms)')


print('\nDECRYPTION TIME FOR THE PROPOSED RSA AND COUNTER CTR')
start_time2 = time.time()
x, decrypt_time=crypo.decrypt(5 , '1234567891234567')
end_time2 = time.time()
# decrypt_time =(end_time2-start_time2)*1000
print(f'Decryption Time (one record (0.081KB)========>, {decrypt_time} (ms)')
print(f'Decryption Time (ALL record (12KB)========>, {decrypt_time*155} (ms)')
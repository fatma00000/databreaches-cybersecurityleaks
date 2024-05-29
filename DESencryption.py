
from Crypto.Cipher import DES
import random


def keygen(x,r,size):
    key = []
    for i in range(size):
        x = r*x*(1-x)
        key.append(x)    
    for i in range(size):
        q = random.random()
        if q<key[i]:
            key[i] = 1
        else:
            key[i] = 0
    key_str = ''.join(map(str, key))
    #print(key_str);input()
    key_int = int(key_str, 2)
    key_byte = key_int.to_bytes(8, byteorder='big')
    
    return key_byte


key = keygen(0.001,3.915,64)

cipher = DES.new(key, DES.MODE_ECB)

f = open('dataset1.txt', 'r')
plaintext = f.read()
f.close()

print("Plain text: ",plaintext)
pad_size = 8-(len(plaintext)%8)
plaintext = plaintext+'0'*pad_size
enc_msg = cipher.encrypt(bytes(plaintext, 'utf-8'))
print("Enc Msg: ", enc_msg.decode('latin-1', errors='ignore'))



dec_msg= cipher.decrypt(enc_msg)
dec_msg = dec_msg[:-pad_size]

print("Dec Msg:",dec_msg.decode('latin-1', errors='ignore') )


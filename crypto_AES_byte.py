from hashlib import md5
from base64 import b64decode
from base64 import b64encode
from Cryptodome import Random
from Cryptodome.Cipher import AES


BLOCK_SIZE = 32  # Bytes

# Padding and padding removal functions
pad = lambda s: s + (BLOCK_SIZE - len(s) % BLOCK_SIZE) * b'Z'
def unpad(s):
    while s[len(s)-1] == 90:
        s = s[:-1]
        if(len(s)==0):
            break
    return s

class AESCipher_bytes:

    def __init__(self, key):
        # Hashed pass phrase
        self.key = md5(key.encode('utf8')).hexdigest().encode()

    def encrypt(self, raw):
        raw = pad(raw)
        iv = Random.new().read(AES.block_size)
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return b64encode(iv + cipher.encrypt(raw))

    def decrypt(self, enc):
        enc = b64decode(enc)
        iv = enc[:AES.block_size]
        cipher = AES.new(self.key, AES.MODE_CBC, iv)
        return unpad(cipher.decrypt(enc[AES.block_size:]))


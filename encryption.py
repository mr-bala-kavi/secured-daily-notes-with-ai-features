from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os
import base64

SECRET_KEY = b"01234567890123456789012345678901"


def encrypt_text(text):
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, SECRET_KEY[:16])
    encrypted_data = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv + encrypted_data).decode()

def decrypt_text(encrypted_text):
    encrypted_data = base64.b64decode(encrypted_text)
    iv = encrypted_data[:16]
    cipher = AES.new(SECRET_KEY, AES.MODE_CBC, iv)
    return unpad(cipher.decrypt(encrypted_data[16:]), AES.block_size).decode()

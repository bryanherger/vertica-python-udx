from os import urandom
from Crypto.Cipher import AES
import base64

# For Generating cipher text
secret_key = b'0123456789abcdef'
iv = b'0123456789abcdef'
obj = AES.new(secret_key, AES.MODE_CBC, iv)

# Encrypt the message
message = b'Lorem Ipsum text'
print('Original message is: ', message)
encrypted_text = obj.encrypt(message)
print('The encrypted text', encrypted_text)
print('base64',base64.b64encode(encrypted_text))
# Decrypt the message
rev_obj = AES.new(secret_key, AES.MODE_CBC, iv)
decrypted_text = rev_obj.decrypt(encrypted_text)
print('The decrypted text', decrypted_text.decode('utf-8'))


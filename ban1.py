import os
import pickle

# Issue 1: Hardcoded Secret
password = "mysecretpassword"
print(f"Password: {password}")

# Issue 2: Command Injection
user_input = input("Enter a command: ")
os.system(user_input)  # Simulate a dangerous command execution

# Issue 3: Insecure Deserialization
serialized_data = b'\x80\x03U\x05adminq\x00.'
loaded_data = pickle.loads(serialized_data)  # Simulate a deserialization vulnerability

# Issue 4: Insecure Use of Cryptography
from cryptography.fernet import Fernet

key = "insecure_key"
cipher_suite = Fernet(key)
text = "SensitiveData123"
cipher_text = cipher_suite.encrypt(text.encode())

print(f"Cipher Text: {cipher_text.decode()}")

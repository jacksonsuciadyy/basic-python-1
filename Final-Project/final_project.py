#####################################################################################
#                                                                                   #
# Reference :                                                                       #
#   - https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/         #
#   - https://realpython.com/python-send-email/                                     #
#                                                                                   #
#####################################################################################

import os
import smtplib
from getpass import getpass
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

username = ""
password = ""
subject = ""

# Get Emails from receiver_list.txt
def getEmails():
    f = open("receiver_list.txt", "r")
    return f.readlines()

# Get Email Body from email_body.txt
def getEmailBody():
    with open("email_body.txt", 'r') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# Get Attachment to Send
def getAttachment():
    # File must be in the same directory
    filename = "receiver_list.txt"

    # Open File in Binary Mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {filename}",
    )
    return part

# Set-Up SMTP server
def setUpSMTP():
    s = smtplib.SMTP('smtp.gmail.com:587')
    s.ehlo()
    s.starttls()
    s.login(username, password)
    return s

# Send Email
def sendEmail(emails, emailBody):
    try:
        s = setUpSMTP()
        for email in emails:
            # print(email)

            # Create a Message
            msg = MIMEMultipart()

            # Convert Param in Email Body
            message = emailBody.substitute(EMAIL = email)

            # Set-Up Parameters of the Message ( From, To, Subject )
            msg['From'] = username
            msg['To'] = email
            msg['Subject'] = subject

            # Add message into msg
            msg.attach(MIMEText(message, 'plain'))

            # Add attachment into msg
            msg.attach(getAttachment())

            # Send Message
            s.send_message(msg)
            
            # Delete msg object
            del msg

    except Exception as e: 
        print(e)
    else:
        print("Email sukses terkirim!")

def main():
    os.chdir('./Final-Project')
    
    # Input SMTP Username & From Email
    global username
    username = input("Username: ")

    # Input SMTP Password
    global password
    password = getpass()

    # Input Subject
    global subject
    subject = input("Subject: ")

    emails = getEmails()

    emailBody = getEmailBody()

    sendEmail(emails, emailBody)

main()
# import time
# import smtplib
# import datetime
# from shutil import copyfile
# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart
from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'dddd@gmail.com' #Email of sender goes here
email_password = '' #password goes here
email_receivers = {
    1 :'ZVZXVXC4@gmail.com',
    2 : 'XDFDSFDF@gmail.com',
    3 : 'XDSDD@gmail.com',
    4 : 'SDFDD@gmail.com'} # Dictionary containing emails of receivers

subject = 'Finish the Tkinter project'      #Subject of Email

body = """                           
 Complete it now!!!!!!!
 """            #Body of Email
x=1
while x < len(email_receivers):    
    email=EmailMessage()
    email['From'] = email_sender
    email['To'] = email_receivers[x]
    email['subject'] = subject
    email.set_content(body)
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(email_sender, email_password)
        smtp.sendmail(email_sender, email_receivers[x], email.as_string())
        x=x+1
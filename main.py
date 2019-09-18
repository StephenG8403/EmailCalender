#Stephen Gaydash
#Body of code for API and sorting.
print("Hello! This is the main body of code for the program.")

import smtplib

import config

def send.email(subject, msg):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.EMAIL_ADRESS, config.PASSWORD)
        message = 'Subject: {}/m/m{}'.format(subject, msg)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("sucess!")
    except:
        print("failure!")

subject = "Hello!"
msg = "Hello, how are you?"

send_email(subject, msg)

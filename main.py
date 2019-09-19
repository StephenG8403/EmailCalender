#Stephen Gaydash
#Body of code for API and sorting.
print("Hello! This is the main body of code for the program.")
import smtplib, ssl
import config
smtp_server = ('smtp.gmail.com')
port = 587 #used for starttls
message ="""\
Subject: Test

Hello sir.

"""

try:
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()
        server.starttls(context=context)
        server.login(config.EMAIL_ADDRESS, config.PASSWORD)
        server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
        server.quit()
        print("success!")
except:
    print("failure!")



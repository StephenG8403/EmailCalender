#Stephen Gaydash
#Body of code for API and sorting.
print("Hello! This is the main body of code for the program.")
import smtplib
port: 56556 #for ssl
import config
def send_email(subject, msg):
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.login(config.EMAIL_ADDRESS, config.PASSWORD)
            message = 'Subject: {}/m/m{}'.format(subject, msg)
            server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS, message)
            server.quit()
            print("sucess!")
        except:
            print("failure!")
subject = "Hello!"
message: str = "Hello, how are you?"
def send_email(subject,message):
    pass



send_email(message, str)

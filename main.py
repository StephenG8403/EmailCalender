#Stephen Gaydash
#Body of code for API and sorting.
print("Hello! This is the main body of code for the program.")
import smtplib, ssl
import config
emailServer = input('Which email do you use? (Gmail, Outlook, Yahoo)')
subject = input('Subject:')
msg = input('Message:')
message = (subject, msg)
if emailServer == ("Gmail"):
    smtp_server = ('smtp.gmail.com')
    port = 587  # used for starttls
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.login(config.EMAIL_ADDRESS, config.PASSWORD)
            server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS_TO, message)
            server.quit()
            print("success!")
    except:
        print("failure!")
elif emailServer == ('Outlook'):
    smtp_server = 'smtp-mail.outlook.com'
    port = 587
    try:
        context = ssl.create_default_context()
        with smtplib.SMTP(smtp_server, port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.login(config.EMAIL_ADDRESS, config.PASSWORD)
            server.sendmail(config.EMAIL_ADDRESS, config.EMAIL_ADDRESS_TO, message)
            server.quit()
            print("success!")
    except:
        print("failure!")




#Stephen Gaydash
#Body of code for API and sorting.
print("Hello! This is the main body of code for the program.")
import smtplib, ssl
import config
emailServer = input('Which email do you use? (Gmail = 1, Outlook = 2, Yahoo = 3)')
subject = input('Subject:')
msg = input('Message:')
message = (subject, msg)
if emailServer == ("1"):
    smtp_server = ('smtp.gmail.com')
    port = 587  # used for starttls
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



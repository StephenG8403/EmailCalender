#Stephen Gaydash
#Body of code for API and sorting.
print("Hello! This is the main body of code for the program.")
import smtplib, ssl
sendReceive = input('Would you like to send or receive emails? (Send, Receive)')
if sendReceive == ('Send'):
    import config
    invalidInput = True
    def start():
        emailServer = input('Which email do you use? (Gmail, Outlook, Yahoo)')
        EMAIL_ADDRESS_TO = input('Recipient:')
        subject = input('Subject:')
        msg = input('Message:')
        message = (subject, msg)
        if emailServer == ("Gmail"):
            invalidInput = False
            smtp_server = ('smtp.gmail.com')
            port = 587  # used for starttls
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()
                    server.starttls(context=context)
                    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
                    server.sendmail(config.EMAIL_ADDRESS, EMAIL_ADDRESS_TO, message)
                    server.quit()
                    print("success!")
                    repeat = input('Send another email? (Yes or No)')
                    if repeat == ('Yes'):
                            invalidInput = True
                    elif repeat == ('No'):
                            quit()
            except:
                print("failure!")
                repeat = input('Try again? (Yes or No')
                if repeat == ('Yes'):
                    invalidInput = True
                elif repeat == ('No'):
                    quit()
        elif emailServer == ('Outlook'):
            invalidInput = False
            EMAIL_ADDRESS_TO = input('Recipient:')
            smtp_server = 'smtp-mail.outlook.com'
            port = 587
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()
                    server.starttls(context=context)
                    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
                    server.sendmail(config.EMAIL_ADDRESS, EMAIL_ADDRESS_TO, message)
                    server.quit()
                    print("success!")
            except:
                print("failure!")
                repeat = input('Try again? (Yes or No')
                if repeat == ('Yes'):
                    invalidInput = True
                elif repeat == ('No'):
                    quit()
        elif emailServer == ('Yahoo'):
            invalidInput = False
            EMAIL_ADDRESS_TO = input('Recipient:')
            smtp_server = 'smtp.mail.yahoo.com'
            port = 587
            try:
                context = ssl.create_default_context()
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()
                    server.starttls(context=context)
                    server.login(config.EMAIL_ADDRESS, config.PASSWORD)
                    server.sendmail(config.EMAIL_ADDRESS, EMAIL_ADDRESS_TO, message)
                    server.quit()
                    print("success!")
            except:
                print("failure!")
                repeat = input('Try again? (Yes or No')
                if repeat == ('Yes'):
                    invalidInput = True
                elif repeat == ('No'):
                    quit()
        elif print('Sorry, invalid command.'):
            invalidInput = True
    while invalidInput == True:
        start()
elif sendReceive == ('Receive'):
    import poplib
    from email import parser
    import config
    config.EMAIL_ADDRESS_TO = ('null')
    receiveEmailServer = input('Which email do you use? (Gmail, Outlook, Yahoo)')
    if receiveEmailServer == ('Gmail'):
        pop_conn = poplib.POP3_SSL('pop.gmail.com')
        pop_conn.user = (config.EMAIL_ADDRESS)
        pop_conn.pass_(config.PASSWORD)
        messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1])+1)]
        messages = ["\n".join(mssg[1]) for mssg in messages]
        messages = [parser.Parser().parsestr(mssg) for mssg in messages]
        for message in messages:
            print(message['subject'])
            print(message.get_payload())
        pop_conn.quit()

# Stephen Gaydash
# Body of code for API and sorting.
print("Hello! This is the main body of code for the program.")
import smtplib
import ssl
invalidBegin = True
# this begins the send/receive block
def begin():
    sendReceive = input('Would you like to send or receive emails? (Send, Receive)')
    if sendReceive == ('Send') or sendReceive == ('send'):
        invalidBegin = False
        print('Enter login information')
        EMAIL_ADDRESS = input('Email Address:')
        PASSWORD = input('Password:')
        invalidInput = True
        def start():
            emailServer = input('Which email do you use? (Gmail, Outlook, Yahoo)')
            if emailServer == ('Gmail') or emailServer == ('gmail'): #this begins the gmail smtp block
                invalidInput = False
                emailAddressTo = input('Recipient:')
                subject = input('Subject:')
                message = input('Message:')
                smtp_server = 'smtp.gmail.com'
                port = 587  # used for starttls
                try:
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        server.starttls(context=context)
                        server.login(EMAIL_ADDRESS, PASSWORD)
                        server.sendmail(EMAIL_ADDRESS, emailAddressTo, message + subject)
                        server.quit()
                        print("success!")
                        repeat = input('Send another email? (Yes or No)')
                        if repeat == ('Yes') or repeat == ('yes'):
                            invalidInput = True
                        elif repeat == ('No') or repeat == ('no'):
                            quit()
                except:
                    print("failure!")
                    repeat = input('Try again? (Yes or No)')
                    if repeat == ('Yes') or repeat == ('yes'):
                        invalidInput = True
                    elif repeat == ('No') or repeat == ('no'):
                        quit()
            elif emailServer == ('Outlook') or emailServer == ('outlook'): #this begins the outlook smtp block
                invalidInput = False
                EMAIL_ADDRESS_TO = input('Recipient:')
                subject = input('Subject:')
                msg = input('Message:')
                message = (subject, msg)
                smtp_server = 'smtp-mail.outlook.com'
                port = 587
                try:
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        server.starttls(context=context)
                        server.login(EMAIL_ADDRESS, PASSWORD)
                        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS_TO, message)
                        server.quit()
                        print("success!")
                        repeat = input('Send another email? (Yes or No)')
                        if repeat == ('Yes') or repeat == ('yes'):
                            invalidInput = True
                        elif repeat == ('No') or repeat == ('no'):
                            quit()
                except:
                    print("failure!")
                    repeat = input('Try again? (Yes or No)')
                    if repeat == ('Yes') or repeat == ('yes'):
                        invalidInput = True
                    elif repeat == ('No') or repeat == ('no'):
                        quit()
            elif emailServer == ('Yahoo') or emailServer == ('yahoo'): #this begins the yahoo smtp block
                invalidInput = False
                EMAIL_ADDRESS_TO = input('Recipient:')
                subject = input('Subject:')
                msg = input('Message:')
                message = (subject, msg)
                smtp_server = 'smtp.mail.yahoo.com'
                port = 587
                try:
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        server.starttls(context=context)
                        server.login(EMAIL_ADDRESS, PASSWORD)
                        server.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS_TO, message)
                        server.quit()
                        print("success!")
                        repeat = input('Send another email? (Yes or No)')
                        if repeat == ('Yes') or repeat == ('yes'):
                            invalidInput = True
                        elif repeat == ('No') or repeat == ('no'):
                            quit()
                except:
                    print("failure!")
                    repeat = input('Try again? (Yes or No)')
                    if repeat == ('Yes') or repeat == ('yes'):
                        invalidInput = True
                    elif repeat == ('No') or repeat == ('no'):
                        quit()
            elif print('Sorry, invalid command.'):
                invalidInput = True
        while invalidInput == True:
            start()
    elif sendReceive == ('Receive') or sendReceive == ('receive'):
        invalidBegin = False
        import poplib
        from email import parser
        #EMAIL_ADDRESS_TO = ('null')
        EMAIL_ADDRESS = input('Email Address:')
        PASSWORD = input('Password:')
        receiveEmailServer = input('Which email do you use? (Gmail, Outlook, Yahoo)')
        if receiveEmailServer == ('Gmail'):
            pop_conn = poplib.POP3_SSL('pop.gmail.com')
            pop_conn.user = (EMAIL_ADDRESS)
            pop_conn.pass_(PASSWORD)
            messages = [pop_conn.retr(i) for i in range(1, len(pop_conn.list()[1]) + 1)]
            messages = ["\n".join(mssg[1]) for mssg in messages]
            messages = [parser.Parser().parsestr(mssg) for mssg in messages]
            for message in messages:
                print(message['subject'])
                print(message.get_payload())
            pop_conn.quit()
    elif print('Sorry, invalid command.'):
        invalidBegin = True
while invalidBegin == True:
    begin()

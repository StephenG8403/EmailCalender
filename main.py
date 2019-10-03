# Stephen Gaydash
# Body of code for API and sorting.
print("Hello! This is the main body of code for the program.")
import smtplib
import ssl



# this begins the send/receive block
#global invalidBegin
def begin():
    sendReceive = input('Would you like to send or receive emails? (Send, Receive)')
    while invalidBegin == True:
        begin()
        if sendReceive == 'Send' or sendReceive == 'send':
            invalidBegin = False

            def start():
                emailServer = input('Which email do you use? (Gmail, Outlook, Yahoo)')
                print('Enter login information')
                EMAIL_ADDRESS = input('Email Address:')
                PASSWORD = input('Password:')
                while invalidInput == True:
                    start()
                    if emailServer == 'Gmail' or emailServer == 'gmail':  # this begins the gmail smtp block
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
                                if repeat == 'Yes' or repeat == 'yes':
                                    invalidInput = True
                                elif repeat == 'No' or repeat == 'no':
                                    quit()
                        except:
                            print("failure!")
                            repeat = input('Try again? (Yes or No)')
                            if repeat == 'Yes' or repeat == 'yes':
                                invalidInput = True
                            elif repeat == 'No' or repeat == 'no':
                                quit()
                    elif emailServer == 'Outlook' or emailServer == 'outlook':  # this begins the outlook smtp block
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
                                if repeat == 'Yes' or repeat == 'yes':
                                    invalidInput = True
                                elif repeat == 'No' or repeat == 'no':
                                    quit()
                        except:
                            print("failure!")
                            repeat = input('Try again? (Yes or No)')
                            if repeat == 'Yes' or repeat == 'yes':
                                invalidInput = True
                            elif repeat == 'No' or repeat == 'no':
                                quit()
                    elif emailServer == 'Yahoo' or emailServer == 'yahoo':  # this begins the yahoo smtp block
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
                                if repeat == 'Yes' or repeat == 'yes':
                                    invalidInput = True
                                elif repeat == 'No' or repeat == 'no':
                                    quit()
                        except:
                            print("failure!")
                            repeat = input('Try again? (Yes or No)')
                            if repeat == 'Yes' or repeat == 'yes':
                                invalidInput = True
                            elif repeat == 'No' or repeat == 'no':
                                quit()
                    elif print('Sorry, invalid command.'):
                        invalidInput = True
        elif sendReceive == 'Receive' or sendReceive == 'receive':
            invalidBegin = False
            import poplib
            from email import parser
            # EMAIL_ADDRESS_TO = ('null') NOT NEEDED FOR RECEIVE
            receiveEmailServer = input('Which email do you use? (Gmail, Outlook, Yahoo)')
            EMAIL_ADDRESS = input('Email Address:')
            PASSWORD = input('Password:')
            if receiveEmailServer == 'Gmail' or receiveEmailServer == 'gmail':
                try:
                    context = ssl.create_default_context()
                    pop3 = poplib.POP3_SSL('pop.gmail.com', 995)
                    # pop3.stls(context=context)
                    pop3.user(EMAIL_ADDRESS)
                    pop3.pass_(PASSWORD)
                    messages = [pop3.retr(i) for i in range(1, len(pop3.list()[1]) + 1)]
                    messages = []
                    for mssg in messages:
                        messages.append("\n".join(mssg[1]))
                    messages = [parser.Parser().parsestr(mssg) for mssg in messages]
                    for message in messages:
                        print(message['subject'])
                        print(message.get_payload())
                    pop3.quit()
                    print('Success.')
                    receiveRepeat = input('Receive another message? (Yes or No)')
                    if receiveRepeat == 'Yes' or receiveRepeat == 'yes':
                        invalidBegin = True
                    elif receiveRepeat == 'No' or receiveRepeat == 'no':
                        quit()
                except:
                    print('Failure in retreiving message.')
                    receiveRetry = input('Try again? (Yes or No)')
                    if receiveRetry == 'Yes' or receiveRetry == 'yes':
                        invalidBegin = True
                    elif receiveRetry == 'No' or receiveRetry == 'no':
                        print('Ok')
                        quit()
            elif receiveEmailServer != 'gmail' or receiveEmailServer != 'Gmail':
                print('Sorry invalid command.')
                invalidBegin = True
        elif sendReceive != 'Send' or sendReceive != 'send' or sendReceive != 'Receive' or sendReceive != 'receive':
            print('Sorry, invalid command.')
            invalidBegin = True
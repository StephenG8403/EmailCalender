# Stephen Gaydash
# Body of code for API and sorting.
print("Hello! This is the main body of code for the program.")
import smtplib
import ssl
from tkinter import *

# this begins the send/receive block
# global invalidBegin #### NOT NEEDED

root = Tk()


#### background globally
# photo1 = PhotoImage(file='background.jpeg')
# theBackground = Label(window, image=photo1, bg='black') .grid(row=0, column=0, sticky='W')

send_receive = input('Would you like to send or receive emails? (Send, Receive)')
if send_receive == 'Send' or send_receive == 'send':
    # invalid_begin = False
    # loginRepeat = False ####FOR LATER FEATURE
    def start():
        email_server = input('Which email do you use? (Gmail, Outlook, Yahoo)')
        print('Enter login information')
        email_address = input('Email Address:')
        password = input('Password:')
        invalid_input = True
        while invalid_input:
            if email_server == 'Gmail' or email_server == 'gmail':  # this begins the gmail smtp block
                # invalid_input = False NOT NEEDED
                email_address_to = input('Recipient:')
                subject = input('Subject:')
                message = input('Message:')
                smtp_server = 'smtp.gmail.com'
                port = 587  # used for starttls
                try:
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        server.starttls(context=context)
                        server.login(email_address, password)
                        server.sendmail(email_address, email_address_to, message + subject)
                        server.quit()
                        print("success!")
                        repeat = input('Send another email? (Yes or No)')
                        if repeat == 'Yes' or repeat == 'yes':
                            print('Ok')
                        elif repeat == 'No' or repeat == 'no':
                            invalid_input = False
                except:
                    print("failure!")
                    repeat = input('Try again? (Yes or No)')
                    if repeat == 'Yes' or repeat == 'yes':
                        print('Ok')
                    elif repeat == 'No' or repeat == 'no':
                        invalid_input = False
            elif email_server == 'Outlook' or email_server == 'outlook':  # this begins the outlook smtp block
                invalid_input = False
                email_address_to = input('Recipient:')
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
                        server.login(email_address, password)
                        server.sendmail(email_address, email_address_to, message)
                        server.quit()
                        print("success!")
                        repeat = input('Send another email? (Yes or No)')
                        if repeat == 'Yes' or repeat == 'yes':
                            print('Ok')
                        elif repeat == 'No' or repeat == 'no':
                            invalid_input = False
                except:
                    print("failure!")
                    repeat = input('Try again? (Yes or No)')
                    if repeat == 'Yes' or repeat == 'yes':
                        print('Ok')
                    elif repeat == 'No' or repeat == 'no':
                        invalid_input = False
            elif email_server == 'Yahoo' or email_server == 'yahoo':  # this begins the yahoo smtp block
                invalid_input = False
                email_address_to = input('Recipient:')
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
                        server.login(email_address, password)
                        server.sendmail(email_address, email_address_to, message)
                        server.quit()
                        print("success!")
                        repeat = input('Send another email? (Yes or No)')
                        if repeat == 'Yes' or repeat == 'yes':
                            print('Ok')
                        elif repeat == 'No' or repeat == 'no':
                            invalid_input = True
                except:
                    print("failure!")
                    repeat = input('Try again? (Yes or No)')
                    if repeat == 'Yes' or repeat == 'yes':
                        print('Ok')
                    elif repeat == 'No' or repeat == 'no':
                        invalid_input = False
            elif print('Sorry, invalid command.'):
                print('Returning')
elif send_receive == 'Receive' or send_receive == 'receive':
    def readmail():
        invalid_begin = True
        while invalid_begin:
            import poplib
            from email import parser
            # EMAIL_ADDRESS_TO = ('null') NOT NEEDED FOR RECEIVE
            receive_email_server = input('Which email do you use? (Gmail, Outlook, Yahoo)')
            email_address = input('Email Address:')
            password = input('Password:')
            if receive_email_server == 'Gmail' or receive_email_server == 'gmail':
                try:
                    # context = ssl.create_default_context()
                    pop3 = poplib.POP3_SSL('pop.gmail.com', 995)
                    # pop3.stls(context=context)
                    pop3.user(email_address)
                    pop3.pass_(password)
                    messages = [pop3.retr(i) for i in range(1, len(pop3.list()[1]) + 1)]
                    # messages = []
                    for mssg in messages:
                        messages.append("\n".join(mssg[1]))
                    messages = [parser.Parser().parsestr(mssg) for mssg in messages]
                    for message in messages:
                        print(message['subject'])
                        print(message.get_payload())
                    pop3.quit()
                    print('Success.')
                    receive_repeat = input('Receive another message? (Yes or No)')
                    if receive_repeat == 'Yes' or receive_repeat == 'yes':
                        print('Ok')
                    elif receive_repeat == 'No' or receive_repeat == 'no':
                        invalid_begin = False
                except:
                    print('Failure in retrieving message.')
                    receive_retry = input('Try again? (Yes or No)')
                    if receive_retry == 'Yes' or receive_retry == 'yes':
                        print('Ok')
                    elif receive_retry == 'No' or receive_retry == 'no':
                        invalid_begin = False
            elif receive_email_server != 'gmail' or receive_email_server != 'Gmail':
                print('Sorry, invalid command.')
                invalid_begin = False
            elif send_receive != 'Send' or send_receive != 'send' or send_receive != 'Receive' or send_receive != 'receive':
                print('Sorry, invalid command.')
                invalid_begin = False
        readmail()
start()
class gui:
    frame = Frame(root)


root.mainloop(gui())


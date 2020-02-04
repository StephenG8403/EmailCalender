# Stephen Gaydash
# Body of code for API and sorting.
print("Hello! This is the main body of code for the program.")
import smtplib
import ssl
import time


# from tkinter import *

# this begins the send/receive block
# global invalidBegin #### NOT NEEDED

#### root = Tk()                FOR KIVY


#### background globally                FOR KIVY
# photo1 = PhotoImage(file='background.jpeg')
# theBackground = Label(window, image=photo1, bg='black') .grid(row=0, column=0, sticky='W')
def internet():
    import imaplib
    smtp_server = 'smtp.gmail.com'
    port = 587  # used for starttls
    host = 'imap.gmail.com'
    imapport = 993  # used for starttls
    print('We will now test your connection with the SMTP and IMAP server.')
    testcon = input('Test connection? (Yes or No)')
    if testcon == 'Yes' or testcon == 'yes':
        time.sleep(2)
        print('.')
        time.sleep(2)
        print('.')
        try:
            context = ssl.create_default_context(purpose=A)  #### Check server connection block
            def con():
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()
                    server.starttls(context=context)
                    server.quit()
                    print('SMTP works!')
                    try:
                        with imaplib.IMAP4_SSL(host, imapport) as server:
                            server.noop()
                            server.starttls(ssl_context=context)
                            server.logout()
                            print('IMAP works!')
                            time.sleep(1)
                            print('Success!')
                            prog()
                    except:
                        print('IMAP connection has failed!')
                        print('Please try again.')
                        internet()

            con()

        except:
            print('Sorry, we were unable to connect with the SMTP and IMAP server.')
            time.sleep(2)
            print('Please check your connection to the internet and try again.')
            internet()
    elif testcon == 'No' or testcon == 'no':
        quit()
    else:
        print('Sorry, you have input an invalid command. Please try again!')


def prog():
    def start():
        invalid_input = True
        email_server = input('Which email do you use? (Gmail, Outlook, Yahoo)')

        while invalid_input:  #### USED FOR TEST BLOCK
            if email_server == 'Gmail' or email_server == 'gmail':  # this begins the gmail smtp block
                print('Enter login information')
                email_address = input('Email Address:')
                password = input('Password:')
                smtp_server = 'smtp.gmail.com'
                port = 587  # used for starttls

                def execute():
                    email_address_to = input('Recipient:')
                    subject = input('Subject:')
                    message = input('Message:')
                    messagesubject = str(message) + str(subject)

                    try:
                        context = ssl.create_default_context()
                        with smtplib.SMTP(smtp_server, port) as server:
                            server.ehlo()
                            server.starttls(context=context)
                            server.login(email_address, password)
                            server.sendmail(email_address, email_address_to, messagesubject)
                            server.quit()
                            print("success!")
                            repeat = input('Send another email? (Yes or No)')
                            if repeat == 'Yes' or repeat == 'yes':
                                print('Ok')
                                execute()
                            elif repeat == 'No' or repeat == 'no':
                                quit()
                    except:
                        print("failure!")
                        repeat = input('Try again? (Yes or No)')
                        if repeat == 'Yes' or repeat == 'yes':
                            print('Ok')
                            start()
                        elif repeat == 'No' or repeat == 'no':
                            quit() ## doesnt work????? maybe??? cant test rn

                try:
                    context = ssl.create_default_context()
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        server.starttls()
                        server.login(email_address, password)
                        server.quit()
                        execute()
                except:
                    print('Invalid Login. Please try again.')
                    invalid_input = False
                    start()

                    ####END TEST BLOCK


            elif email_server == 'Outlook' or email_server == 'outlook':  # this begins the outlook smtp block NEED TO REFORMAT TO MATCH GMAIL BLOCK
                invalid_input = False
                print("Enter login information")
                email_address = input('Email Address:')
                password = input('Password:')

                smtp_server = 'smtp-mail.outlook.com'
                port = 587

                def executeout():
                    email_address_to = input('Recipient:')
                    subject = input('Subject:')
                    msg = input('Message:')
                    message = (subject, msg)
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
                                executeout()
                            elif repeat == 'No' or repeat == 'no':
                                quit()
                    except:
                        print("failure!")
                        repeat = input('Try again? (Yes or No)')
                        if repeat == 'Yes' or repeat == 'yes':
                            print('Ok')
                            start()
                        elif repeat == 'No' or repeat == 'no':
                            quit()

                try:
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        server.starttls(context=context)
                        server.login(email_address, password)
                        server.quit()
                        executeout()
                except:
                    print('Invalid Login. Please try again.')
                    invalid_input = False
                    start()


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
                            start()
                        elif repeat == 'No' or repeat == 'no':
                            quit()
                except:
                    print("failure!")
                    repeat = input('Try again? (Yes or No)')
                    if repeat == 'Yes' or repeat == 'yes':
                        print('Ok')
                        start()
                    elif repeat == 'No' or repeat == 'no':
                        quit()
            elif print('Sorry, invalid command.'):
                print('Returning')
                start()

    def readmail():
        invalid_begin = True
        while invalid_begin:
            import imaplib
            from imaplib import IMAP4
            import socket
            # EMAIL_ADDRESS_TO = ('null') NOT NEEDED FOR RECEIVE
            receive_email_server = input('Which email do you use? (Gmail, Outlook, Yahoo)')
            email_address = input('Email Address:')
            password = input('Password:')
            if receive_email_server == 'Gmail' or receive_email_server == 'gmail':
                try:
                    host = 'imap.gmail.com'
                    port = 993
                    context = ssl.create_default_context()
                    with imaplib.IMAP4_SSL(host, port, ssl_context=ssl.create_default_context()) as server:
                        # socket.create_connection(host, port)
                        server.noop()
                        server.starttls()
                        server.open(host, port)
                        # IMAP4.check('imap.gmail.com')
                        server.login(email_address, password)
                        # IMAP4.fetch
                        server.logout()


                        print('Success.')
                        receive_repeat = input('Receive another message? (Yes or No)')
                        if receive_repeat == 'Yes' or receive_repeat == 'yes':
                            print('Ok')
                            readmail()
                        elif receive_repeat == 'No' or receive_repeat == 'no':
                            invalid_begin = False
                except:
                    print('Failure in retrieving message.')
                    receive_retry = input('Try again? (Yes or No)')
                    if receive_retry == 'Yes' or receive_retry == 'yes':
                        print('Ok')
                        readmail()
                    elif receive_retry == 'No' or receive_retry == 'no':
                        invalid_begin = False
            elif receive_email_server != 'gmail' or receive_email_server != 'Gmail':
                print('Sorry, invalid command.')
                invalid_begin = False

    send_receive = input('Would you like to send or receive emails? (Send, Receive)')
    if send_receive == 'Send' or send_receive == 'send':
        start()
    elif send_receive == 'Receive' or send_receive == 'receive':
        readmail()
    elif send_receive != 'Send' or send_receive != 'send' or send_receive != 'Receive' or send_receive != 'receive':
        print('Sorry, invalid command.')
        invalid_begin = False
        prog()


internet()
####class gui:              FOR KIVY
####frame = Frame(root)


#### root.mainloop(gui())           FOR KIVY

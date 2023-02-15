# Stephen Gaydash
# Body of code for API and sorting.
# 2/15/2023 while loops need to be removed. They seem useless and complicate order tree.
print("Hello! This is the main body of code for the program.")
import smtplib
import ssl
import time

from tkinter import *  ##      <-- will be needed soon, do not remove


# this begins the send/receive block
# global invalidBegin #### NOT NEEDED, remove from all other blocks

#### root = Tk()                FOR KIVY


#### background globally                FOR KIVY
# photo1 = PhotoImage(file='background.jpeg')
# theBackground = Label(window, image=photo1, bg='black') .grid(row=0, column=0, sticky='W')

def globalrules():
    print("GLOBALRULES - this message should be the second line during startup.")
    import imaplib

    ####   this block is used for global command input outside of function blocks
    ####   this function should be called at the bottom of the body of code, if global commands do not work, it is not called.


def prog():
    def start():
        #   invalid_input = True    WHY IS THIS HERE, need to look at commit notes. Removed most instances of this
        #   leaving this piece here just in case
        email_server = input('Which email do you use? (Gmail, Outlook, Yahoo)')

            #   there used to be a while invalid_input: here, should still work without it
        if email_server == 'Gmail' or email_server == 'gmail':  # this begins the gmail smtp block
            def loginblockgmail(): # called from bottom and blocked off for simplicity. copy/paste for other servers
                print('Enter login information')
                email_address = input('Email Address:')
                password = input('Password:')
                smtp_server = 'smtp.gmail.com'
                port = 587  # used for starttls

                def execute():
                    email_address_to = input('Recipient Email:')
                    subjectgmail = input('Subject:')
                    messagegmail = input('Message:')
                    messagesubject = str(messagegmail) + str(subjectgmail)

                    try:
                        context = ssl.create_default_context()
                        with smtplib.SMTP(smtp_server, port) as server:
                            server.ehlo()
                            server.starttls #   removed (context = context), still works.
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
                            quit()  ## works? Previous comment said it did not work. test later

                try:
                    # context = ssl.create_default_context() <-- don't need
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        print("ehlo works")
                        server.starttls
                        print("tls works")
                        server.login(email_address, password)
                        print("login works")
                        server.quit()
                        print("quit works")
                        execute()

                        #   block above not working. I think the server.login is encountering issues.

                except:
                    print('Invalid Login. Please try again.')
                    # invalid_input = False  ##      inside while loop, not needed?
                    loginblockgmail()
            loginblockgmail()
                    ####END TEST BLOCK


        elif email_server == 'Outlook' or email_server == 'outlook':  # this begins the outlook smtp block NEED TO REFORMAT TO MATCH GMAIL BLOCK
            print("Enter login information")
            email_address = input('Email Address:')
            password = input('Password:')

            smtp_server = 'smtp-mail.outlook.com'
            port = 587

            def executeout():
                email_address_to = input('Recipient:')
                subjectoutlook = input('Subject:')
                messageoutlook = input('Message:')
                messagesubject = (subjectoutlook, messageoutlook)
                try:
                    ##  context = ssl.create_default_context() <-- NOT NEEDED
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        server.starttls
                        server.login(email_address, password)
                        server.sendmail(email_address, email_address_to, messagesubject)
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
                    server.starttls
                    server.login(email_address, password)
                    server.quit()
                    executeout()
            except:
                print('Invalid Login. Please try again.')
                invalid_input = False
                start()


        elif email_server == 'Yahoo' or email_server == 'yahoo':  # this begins the yahoo smtp block
            #   invalid_input = False <--- do not need these

            print("Enter login information")
            email_address = input('Email Address:')
            password = input('Password:')

            smtp_server = 'smtp-mail.outlook.com'
            port = 587

            def yahoosendblock():
                email_address_to = input('Recipient:')
                subjectyahoo = input('Subject:')
                messageyahoo = input('Message:')
                messagesubject = (subjectyahoo, messageyahoo)
                smtp_server = 'smtp.mail.yahoo.com'
                port = 587
                try:
                    ##  context = ssl.create_default_context()  <-- NOT NEEDED
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        server.starttls
                        server.login(email_address, password)
                        server.sendmail(email_address, email_address_to, messagesubject)
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

            try:
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()
                    server.starttls
                    server.login(email_address, password)
                    server.quit()
                    yahoosendblock()
            except:
                print('Invalid Login. Please try again.')
                invalid_input = False
                start()
            #   here is where the login test goes for yahoo

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
            #   there used to be a def login block here, removed and code works. add back if code stops working
            receive_email_server = input('Which email do you use? (Gmail, Outlook, Yahoo)')
            if receive_email_server == 'Gmail' or receive_email_server == 'gmail':
                email_address = input('Email Address:')
                password = input('Password:')
                smtp_server = 'smtp.gmail.com'
                port = 587  # used for starttls

                try:
                    with smtplib.SMTP(smtp_server, port) as server:
                        server.ehlo()
                        server.starttls()
                        server.login(email_address, password)
                        server.quit()
                        receivegmail()
                except:
                    print("Incorrect login or code doesn't work - test message at end of receivelogicblock")

            elif receive_email_server == 'Outlook' or receive_email_server == 'outlook':
                print("temp message. this is the outlook receive block")
            else:
                print("Invalid input. Please try again.")
                readmail()
                def receivegmail():
                    try:
                        host = 'imap.gmail.com'
                        port = 993
                        context = ssl.create_default_context()
                        with imaplib.IMAP4_SSL(host, port, ssl_context=ssl.create_default_context()) as server:
                            # certain functions are greyed out to test connection without fetch feature. Keep these here for now.
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
                            receivegmail()
                        elif receive_retry == 'No' or receive_retry == 'no':
                            ##  invalid_begin = False   <-- not sure why this is here
                            start()

    send_receive = input('Would you like to send or receive emails? (Send, Receive)')
    if send_receive == 'Send' or send_receive == 'send':
        start()
    elif send_receive == 'Receive' or send_receive == 'receive':
        readmail()
    elif send_receive != 'Send' or send_receive != 'send' or send_receive != 'Receive' or send_receive != 'receive':
        print('Sorry, invalid command.')
        invalid_begin = False
        start()

def internet():
    import imaplib
    smtp_server = 'smtp.gmail.com'
    port = 587  # used for starttls
    host = 'imap.gmail.com'
    imapport = 993  # used for starttls
    print("You can type 'Home' at any point to bring yourself back to this point") #    implement somehow
    print('We will now test your connection with the SMTP and IMAP server.')
    testcon = input('Test connection? (Yes or No)')
    if testcon == 'Yes' or testcon == 'yes':
        time.sleep(2)
        print('.')
        time.sleep(2)
        print('.')
        try:
            # delete context stuff soon, or figure out why it exists
            # context = ssl.create_default_context(purpose=A)  #### Check server connection block <-- does not work, don't know why I added it
            def con(): # this block is here to clearly define connection testing circuitry. Keep for copy/paste purposes
                with smtplib.SMTP(smtp_server, port) as server:
                    server.ehlo()
                    server.starttls  # (context=context) <-- does not work
                    server.quit()
                    print('SMTP works!')
                    try:
                        with imaplib.IMAP4_SSL(host, imapport) as server:
                            server.noop()
                            server.starttls  # (ssl_context=context) <-- this stuff does not work, don't know why I added it
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
            print('Please check your connection to the internet and restart the program.')
            internet()
    elif testcon == 'No' or testcon == 'no':
        proceed = input("Would you like to proceed? (Internet connection may not be established): Y or N")
        if proceed == "Y" or proceed == "y":
            print("Ok.")
            time.sleep(1)
            prog()
        elif proceed == "N" or proceed == "n":
            print("Ok.")
            time.sleep(1)
            quit()
    else:
        print('Sorry, you have input an invalid command. Please try again!')
        internet()



internet()
####class gui:              FOR KIVY
####frame = Frame(root)


#### root.mainloop(gui())           FOR KIVY

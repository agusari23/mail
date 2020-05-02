import argparse
import getpass
import imaplib
import poplib
import smtplib

#I Wayan Agus Ari Kumara W. P. (170010090)

def imap_mail(username): 
    IMAP_SERVER = 'outlook.office365.com'
    IMAP_PORT = 993
    mailbox = imaplib.IMAP4_SSL(IMAP_SERVER, IMAP_PORT) 
    password = getpass.getpass(prompt='Enter your email password: ') 
    mailbox.login(username, password)
    mailbox.select('Inbox')
    typ, data = mailbox.search(None, 'ALL')
    for num in data[0].split():
        typ, data = mailbox.fetch(num, '(RFC822)')
        print ('Message %s\n%s\n' % (num, data[0][1]))
        break
    mailbox.close()
    mailbox.logout()
    
def pop_mail(username): 
    POP_SERVER = 'outlook.office365.com'
    POP_PORT = 995
    mailbox = poplib.POP3_SSL(POP_SERVER, POP_PORT) 
    mailbox.user(username)
    password = getpass.getpass(prompt='Enter your email password: ') 
    mailbox.pass_(password) 
    num_messages = len(mailbox.list()[1])
    print ('Total emails: {}'.format(num_messages))
    mailbox.quit()

def mail(username, protocol, host, port):
    # Tulis kode program dari sini
    protocol = input("Pilih Menu \n[1].imap_mail \n[2].pop_mail \nPilih nomer: ")
    if protocol == "1":
        imap_mail("170010090@stikom-bali.ac.id")
    else:
        pop_mail("170010090@stikom-bali.ac.id")
    
        # Implementasikan Error-handling

        
    # Sampai di sini

if __name__ == '__main__':
    mail("username","","","")

import email
import getpass
import imaplib
import json
from email.header import decode_header

class EMailWrapper(object): 
    def __init__(self, imap_address, username, password):
        self.imap_address = imap_address 
        self.__username = username
        self.__password = password
        self.fetcher = imaplib.IMAP4_SSL(self.imap_address)

    def login(self):
        self.fetcher.login(self.__username, self.__password)

    def list_mailboxes(self):
        return self.fetcher.list()

    def fetch(self, num, inbox):
        self.fetcher.select(inbox) 
        resp, items = self.fetcher.search(None, "ALL")
        if resp!='OK':
            return "404: Mailbox non-existent!"
        items = items[0].split()
        items.reverse()
        message_dict = {}
        for id in items[:50]:
            msg_resp, data = self.fetcher.fetch(id, "(RFC822)")
            if msg_resp!='OK':
                return "Problem retrieving mail!"
            email_body = data[0][1]
            mail = email.message_from_string(email_body)
            value, charset = decode_header(mail['From'])[0]
            mail_body=[] 
            if mail.is_multipart():
                for msg_part in mail.walk():
                    if msg_part.get_content_type() == 'text/plain':
                        mail_body.append(msg_part.get_payload())
                mail_body = ''.join(mail_body)
            else:
                mail_body = mail.get_payload()

            message_dict[id] = dict(mail.items() + {'Body': mail_body}.items())
            
        return json.dumps(message_dict)

    def __del__(self):
        self.fetcher.logout()


#user = raw_input("Enter your GMail username:")
#pwd = getpass.getpass("Enter your password: ")
#
#a = EMailWrapper("imap.gmail.com", user, pwd)
#a.login()

#f = open('mail', 'w')
#f.write(str(a.fetch(10, 'Inbox')).encode('utf-8'))
#f.close()

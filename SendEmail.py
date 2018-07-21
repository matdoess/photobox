#
# import required modules
#

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.base import MIMEBase
import smtplib
import sys
from base64 import encodebytes
from os.path import basename
# from email import Encoders

from email.header import Header
from email.utils import formataddr


import settings

class SendEmail():
    #
    # declaration of the default mail settings
    #

    # mail address of the sender
    sender = settings.myList['private_config']['mail']['sender']

    # fully qualified domain name of the mail server
    smtpserver = settings.myList['private_config']['mail']['smtpserver']

    # username for the SMTP authentication
    smtpusername = settings.myList['private_config']['mail']['smtpusername']

    # password for the SMTP authentication
    smtppassword = settings.myList['private_config']['mail']['smtppassword']

    # use TLS encryption for the connection
    usetls = True
    
    # def encode_base64(orig):
    #     """Encode the message's payload in Base64.

    #     Also, add an appropriate Content-Transfer-Encoding header.
    #     """
    #     # orig = msg.get_payload()
    #     encdata = _bencode(orig)

    #     # new line inserted to ensure all bytes characters are converted to ASCII
    #     encdata = str(encdata, "ASCII")

    #     msg.set_payload(encdata)
    #     msg['Content-Transfer-Encoding'] = 'base64'

    #     return encdata;

    #
    # function to send a mail
    #
    def sendmail(self, recipient, subject, content, attachementPath):

        author = formataddr((str(Header(u'Photobox', 'utf-8')), self.sender))

        # generate a RFC 2822 message
        msg = MIMEMultipart()
        # msg = MIMEText(content)
        msg['From'] = author
        #msg['From'] = self.sender
        msg['To'] = recipient
        msg['Subject'] = subject

        # open SMTP connection
        server = smtplib.SMTP(self.smtpserver)

        # start TLS encryption
        if self.usetls:
            server.starttls()

        # login with specified account
        if self.smtpusername and self.smtppassword:
            server.login(self.smtpusername,self.smtppassword)

        msg.attach(MIMEText(content))

        # imageFile = file("./pics/2017-10-15_19-11-06_Test.jpg").read()
        imageFile = open(attachementPath, "rb")

        part = MIMEBase('application', "octet-stream")
        part.set_payload(encodebytes(imageFile.read()).decode())
        imageFile.close()
        part.add_header('Content-Transfer-Encoding', 'base64')
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % basename(attachementPath))
        msg.attach(part)   # msg is an instance of MIMEMultipart()

        # part = MIMEBase('application', "octet-stream")
        # part.set_payload(imageFile)

        # encoders.encode_base64(part)
        # msg.attach(part)

        # send generated message
        server.sendmail(self.sender,recipient,msg.as_string())

        # close SMTP connection
        server.quit()


    #
    # main function
    #
    def send(self, sendToAddress, mailContent, attachementPath="./pics/attachement.jpg"):

        # call sendmail() and generate a new mail with specified subject and content
        self.sendmail(sendToAddress, 'Deine Photobox Bilder', mailContent, attachementPath)
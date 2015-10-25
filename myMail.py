#!/usr/bin/env python
# Author: Will Skywalker

# Core Python Pogramming - Unit 17


from smtplib import SMTP
from poplib import POP3
from imaplib import IMAP4
from time import sleep

SMTPSVR = 'smtp.126.com'
POP3SVR = 'pop.126.com'
IMAPSVR = 'imap.126.com'


def send_a_mail(to, sub, body):
    origHdrs = ['From: cxbats@126.com',
                'To: '+to,
                'Subject: '+sub]
    origBody = ['We detacted an unknown face.',
                'Gender: '+body['face'][0]["attribute"]['gender']['value'], 
                'Age: '+str(body['face'][0]["attribute"]['age']['value']),
                'Race: '+body['face'][0]["attribute"]['race']['value']]
    origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),
                               '\r\n'.join(origBody)])

    sendSvr = SMTP(SMTPSVR)
    print 'Sending mail...'
    sendSvr.login('cxbats@126.com', 'nbenbi')
    errs = sendSvr.sendmail('cxbats@126.com', to,
                            origMsg)
    sendSvr.quit()
    print 'Mail sent.'

def welcome_back(to, sub, body):
    origHdrs = ['From: cxbats@126.com',
                'To: '+to,
                'Subject: '+sub]
    origBody = ['Welcome back, Master!',
                'Gender: '+body['face'][0]["attribute"]['gender']['value'], 
                'Age: '+str(body['face'][0]["attribute"]['age']['value']),
                'Race: '+body['face'][0]["attribute"]['race']['value'],
                '\nI love you!']
    origMsg = '\r\n\r\n'.join(['\r\n'.join(origHdrs),
                               '\r\n'.join(origBody)])

    sendSvr = SMTP(SMTPSVR)
    print 'Sending mail...'
    sendSvr.login('cxbats@126.com', 'nbenbi')
    errs = sendSvr.sendmail('cxbats@126.com', to,
                            origMsg)
    sendSvr.quit()
    print 'Mail sent.'



# assert len(errs) == 0, errs
# sleep(10)

# recvSvr = IMAP4(IMAPSVR)
# # recvSvr.user('cxbats@126.com')
# # recvSvr.pass_('nbenbi')
# print 'Receiving mail...'
# recvSvr.login('cxbats@126.com', 'nbenbi')
# recvSvr.select(readonly=True)
# # you haven't see it, you won't remember it
# retcode, msg = recvSvr.search(None, '(UNSEEN)')
# # rsp, msg, siz = recvSvr.retr(recvSvr.stat()[0])

# sep = msg.index('')
# recvBody = msg[sep+1:]
# print recvBody
# assert origBody == recvBody



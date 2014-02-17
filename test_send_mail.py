# -*- coding: utf-8 -*-
import smtplib
import sys
from email.mime.text import MIMEText
from email.utils import formatdate

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: python3 %s [smtp host]' % sys.argv[0])
        quit()

    msg = MIMEText('body')
    msg['Subject'] = 'subject'
    msg['From'] = 'aaa@example.com'
    msg['To'] = 'bbb@example.com'
    msg['Date'] = formatdate()
    s = smtplib.SMTP(sys.argv[1])
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.close()

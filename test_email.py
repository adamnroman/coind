#!/usr/local/bin python3

import smtplib


gmail_user = 'coindproject@gmail.com'
gmail_password = 'byteacademy'
server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
server.ehlo()
server.login(gmail_user,gmail_password)
sent_from = 'coindproject@gmail.com'
to = 'aroman4@u.rochester.edu'
subject = "Your item's price has dropped!"
body = "Your tracked item, {}, has reached your set threshold! Log in to see more details.\n\n -Team Coind".format('test_item')
email_text = """
From: {}
To: {}
Subject: {}

{}
""".format(sent_from, to, subject, body)
server.sendmail(sent_from, to, email_text)
server.close()
print('success')
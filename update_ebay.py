#!/usr/local/bin python3

##This function will update our database for all the items being tracked. Using Crontab

from run.src.models.orm import Database
from run.src.models.url import ebay_getprice
import smtplib

with Database('dealbase.db') as db:
    db.execute("""SELECT * FROM original;""")
    original_data = db.fetchall()  
    for each in original_data:
        db.execute("""SELECT email FROM users WHERE username=?;""",(each[1]))
        email = db.fetchone()
        url = each[5]
        price = ebay_getprice(url)
        db.execute("""INSERT INTO data(
                    username,
                    product,
                    url,
                    price,
                    date) VALUES(
                    ?,
                    ?,
                    ?,
                    ?,
                    datetime('now'));""",(each[1], each[2], url, price))
        ## Now calculate if percentage change was met.
        if price <= (each[4]/100)*each[3]:
            #TODO send notification and mark it on the template
            gmail_user = 'coindproject@gmail.com'
            gmail_password = 'byteacademy'
            server = smtplib.SMTP_SSL('smtp.gmail.com, 465')
            server.ehlo()
            server.login(gmail_user,gmail_password)
            sent_from = 'coindproject@gmail.com'
            to = email[0]
            subject = "Your item's price has dropped!"
            body = "Your tracked item, {}, has reached your set threshold! Log in to see more details.\n\n -Team Coind".format(each[2])
            email_text = """
            From: {}
            To: {}
            Subject: {}

            {}
            """.format(sent_from, to, subject, body)
            server.sendmail(sent_from, to, email_text)
            server.close()
            return "success"
        elif price < each[3]:
            #TODO don't send notification but mark it on website that price has dropped
            return "semi_success"
        else:
            #TODO Make it do nothing i guess
            return "failure"
            
print('done')   






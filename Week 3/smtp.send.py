import smtplib

message = """From: From Joe <joe@low.com>
To: To Naay <naay>
MIME-Version: 1.0
Content-type: text/html
Subject: Test HTML Email

This is a test HTML Message sent as HTML.

<b>This is a test HTML Message.</b>
<h1>This is headling 1</h1>
"""

try:
    smtp = smtplib.SMTP("192.168.89.128")
    smtp.sendmail("naay", "naay", message)
    print("Email sent successfully")
except Exception as err:
    print(str(err))
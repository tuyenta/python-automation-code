" To send HTML customized emails"

import smtplib, ssl, email
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = ""
password = ""

receiver_email = ""

#Create MIMEMultipart object
msg = MIMEMultipart("alternative")
msg["Subject"] = "Email With HTML"
msg["From"] = sender_email
msg["To"] = receiver_email

#HTML Message Part
html = """\
<pre>
    <img src="https://files.schudio.com/parkschool/images/blog/Happy-Birthday-to-you-91.jpg" width="60%" height="50%" />
    <br />
    <h1 style="font-family:Courier New"> Dear SIMON, </h1>
    <h2 style="font-family:Courier New"> Happy birthday!!! <h2>
    <h4 style="font-family:Courier New"> I hope your celebration gives you many happy memories! Wishing you the biggest slice of happy today!!🥳🥳🥳 </h4> <br />

    <h5 style="font-family:Arial">Written With 🧡 By Abhay Parashar <h5>

    <img src="https://media.giphy.com/media/y2J2hwdC4gS7S/giphy.gif" width="350" />
</pre>
"""

part = MIMEText(html, "html")
msg.attach(part)

# Create secure SMTP connection and send email
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(
        sender_email, receiver_email, msg.as_string()
    )
    print("Email Send !!!")
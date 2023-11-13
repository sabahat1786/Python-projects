import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image  import MIMEImage

sender_email = ("sabahat8675@gmail.com")
sender_password = input("your_email_password")
recipient_email = ("seada26@seada.co.uk")
email_subject = "Hello friend"
email_body = "Hi how are you my friend?"

message = MIMEMultipart()
message['From'] = sender_email
message['To'] = recipient_email
message ['subject'] = email_subject
message.attach(MIMEText(email_body, 'plain'))

smtp_object = smtplib.SMTP('smtp.gmail.com', 587)
smtp_object.ehlo()
smtp_object.starttls()
smtp_object.login(sender_email, sender_password)
smtp_object.sendmail(sender_email, recipient_email, message.as_string())
smtp_object.quit()

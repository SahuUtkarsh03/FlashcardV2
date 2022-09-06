from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


SMTP_SERVER_HOST= "localhost"
SMTP_SERVER__PORT= 1025
SENDER_ADDRESS= "Utkarsh@Test.com"
SENDER_PASSWORD= ""

def sendEmail(to,sub,mess):
    msg=MIMEMultipart()
    msg['From'] = SENDER_ADDRESS
    msg['To'] = to
    msg['Subject']=sub

    msg.attach(MIMEText(mess,"plain"))

    try:
        s= smtplib.SMTP(host=SMTP_SERVER_HOST,
                        port=SMTP_SERVER__PORT)
        s.login(SENDER_ADDRESS,SENDER_PASSWORD)
        s.send_message(msg)
        s.quit()
    except :
        return False
    return True
        
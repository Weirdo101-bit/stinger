#sender
import smtplib, ssl
from datetime import datetime
from threading import Timer
from time import *

port = 465
smtp = "mail-serwer64733.lh.pl" 

sender = "pytania@greenstar.net.pl"
password="Ug1nzMMj($X\SQ{0zO@X`}WpP"
reciver="ksiazki@greenstar.net.pl"
subject= datetime.today()
path='log.txt'
f=open(path,"r")
mess=f.read()

message="""Subject: {}
\n
\n 

{}

""".format(subject,mess)
context = ssl.create_default_context()


def send():
	with smtplib.SMTP_SSL(smtp, port, context=context) as server:
	 server.login("pytania@greenstar.net.pl",password)
	 server.sendmail(sender,reciver,message)
	 print("wysłane")

b=0
while b<=5:
	a=10.0
	t=Timer(a,send)
	t.start()
	sleep(a)
	t.cancel()

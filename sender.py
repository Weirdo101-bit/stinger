#sender
import smtplib, ssl

port = 465
smtp = "mail-serwer64733.lh.pl" 

sender = "pytania@greenstar.net.pl"
password="Ug1nzMMj($X\SQ{0zO@X`}WpP"
reciver="ksiazki@greenstar.net.pl"
message="""\ 
Subject: Test \n
\n
This is message from python."""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(smtp, port, context=context) as server:
	 	server.login("pytania@greenstar.net.pl",password)
	 	server.sendmail(sender,reciver,message)
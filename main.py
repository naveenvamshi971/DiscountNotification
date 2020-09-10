import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from bs4 import BeautifulSoup
import urllib.request
import time
def removeComma(s):
	s = s.split(",")
	return "".join(s)
budget=input("enter the budget for the product you want")
budget=float(budget)
Luck=True
at=input("enter the link  of  your product(from amazon)")
you=input("Enter your valid email")
while(Luck):
	x = urllib.request.urlopen(at)
	soup =BeautifulSoup(x,'html.parser')
	a = soup.find('span',id='priceblock_dealprice')
	price=a.text
	price = (removeComma(price))
	price=float(price)
	print(price)
	if price <=budget:
		print("you can buy the product")
		me = "swasthik305@gmail.com"

 		# Create message container - the correct MIME type is multipart/alternative.
		msg = MIMEMultipart('alternative')
		msg['Subject'] = "product notification "
		msg['From'] = me
		msg['To'] = you
		msg.add_header('Content-Type', 'text/html')
 		# Create the body of the message (a plain-text and an HTML version).
		# text = "Hi!\nHow are you?\nHere is the link you wanted:\nhttp://www.python.org"
		html = "hey you can buy your product  now "
	
 		# Record the MIME types of both parts - text/plain and text/html.
		# part1 = MIMEText(text, 'plain')
		part2 = MIMEText(html, 'html')
 		# Attach parts into message container.
		# According to RFC 2046, the last part of a multipart message, in this case
		# the HTML message, is best and preferred.
		# msg.attach(part1)
		msg.attach(part2)
		# Send the message via local SMTP server.
		mail = smtplib.SMTP('smtp.gmail.com', 587)
		mail.ehlo()
		mail.starttls()
		mail.login('swasthik305@gmail.com', '8179634305')
		mail.sendmail(me, you, msg.as_string())
		mail.quit()
		Luck=False
	time.sleep(2) 

#print('hello')
import requests
from bs4 import BeautifulSoup
import smtplib

#amazon link to the product I want to track
URL = "https://www.amazon.com/Dell-P2419HC-Monitor-Full-1080P/dp/B07GBY2M8V/ref=sr_1_3?dchild=1&keywords=usb+c+monitor&qid=1599685165&sr=8-3"

#simply search up "My User-Agent" for the value of the User-Agent key
headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'}

def check_price():
    #get all the information of webpage that I am scraping
    page = requests.get(URL, headers=headers)

    #print('test')

    #parse the page we just requested so we can pull individual pieces of info
    soup = BeautifulSoup(page.content, 'html.parser')

    #look up the price by the id and only print the text and then convert it to only show the int
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = int(price[1:-3])
    #print(converted_price)

    if converted_price != 259:
        send_email()

def send_email():
    #establish connection with gmail server
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    #2-step verification email  password, but you can just add your own pw
    server.login('jrtober11@gmail.com', 'ibkmlafjkgjsgpax')

    subject = 'Price Changed!'
    body = "Check the amazon listing, link: https://www.amazon.com/Dell-P2419HC-Monitor-Full-1080P/dp/B07GBY2M8V/ref=sr_1_3?dchild=1&keywords=usb+c+monitor&qid=1599859519&sr=8-3"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail('jrtober11@gmail.com','jtober@ucsc.edu',msg)

    print('email has been sent')

    #close connection
    server.quit()

check_price() #put in a while True loop to continuoulsy check price like once a day
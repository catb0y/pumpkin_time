#! /usr/bin/python
import feedparser
from twilio.rest import Client
import schedule
import time

# Connecting with Twilio
account_sid = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
twilio_phone_number = '+111111111' #insert given Twilio phone number
my_phone_number = '+1111111111' #insert phone number

client = Client(account_sid, auth_token)

# Scraping Reddit r/GifRecipes
page = feedparser.parse("https://www.reddit.com/r/GifRecipes/.rss")

word = "pumpkin"

# Iterate and send result as text message
def notifier():
    for i in page.entries:
        if word in i.title or word in i.link:
            print "I found something..."
            body = "Pumpkin time! \n{} \n-->{}".format(i.title, i.link)
            client = Client(account_sid, auth_token)
            client.api.account.messages.create(
                body=body,
                to=my_phone_number,
                from_=twilio_phone_number
            )
        else:
            print "whatever"


# Schedule notification
schedule.every(20).minutes.do(notifier)
schedule.every().hours.do(notifier)
schedule.every().day.at("10:30").do(notifier)

while True:
    schedule.run_pending()
    time.sleep(1)



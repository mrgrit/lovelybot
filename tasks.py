from microsoftbotframework import ReplyToActivity
import json
import requests
from datetime import datetime

#def echo_response(message):
#  if message["type"] == "message":
#    ReplyToActivity(fill=message,
#                    text=message["text"]).send()
    
def echo_response(message):  
  if message["type"] == "message" :
    if "bitcoin" in message["text"]:
        now = datetime.now()
        res = requests.get("https://api.korbit-test.com/v1/ticker?currency_pair=btc_krw")
        rej = res.json()
        rep = str(datetime.now()) + 'now' + rej['last'] + 'BTC/KRW.'
        ReplyToActivity(fill=message,
                        text=rep).send()
    else :
        ReplyToActivity(fill=message,
                        text=message["text"]).send()

from flask import Flask, render_template, url_for
from twilio.rest import Client
import config

import os
import puns

app = Flask(__name__)

# Your Account SID from twilio.com/console
account_sid = config.ACCOUNT_SID
# Your Auth Token from twilio.com/console
auth_token  = config.AUTH_TOKEN

client = Client(account_sid, auth_token)

def send_pun():
    pun = puns.generate_random_pun()
    message = client.messages.create(
        to=config.RECIPIENT_NUM,
        from_="+16237380645",
        body=pun)
    # return render_template("home.html")

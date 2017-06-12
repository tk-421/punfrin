from flask import Flask, render_template, url_for
from twilio.rest import Client

import os
import puns

app = Flask(__name__)

# Your Account SID from twilio.com/console
account_sid = os.environ.get('TWILIO_ACCOUNT_SID')
# Your Auth Token from twilio.com/console
auth_token  = os.environ.get('TWILIO_AUTH_TOKEN')

client = Client(account_sid, auth_token)
print os.environ

def send_pun():
    pun = puns.generate_random_pun()
    message = client.messages.create(
        to=os.environ.get('TWILIO_TARGET_NUM'),
        from_=os.environ.get('TWILIO_HOME_NUM'),
        body=pun)
    return pun

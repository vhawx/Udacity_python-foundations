import twilio
print(twilio.__version__)

##https://www.twilio.com//docs/libraries/python

from twilio.rest import *

# Your Account SID from twilio.com/console
account_sid = "AC5f0772c883168073a0aaa9c2d35d5946"
# Your Auth Token from twilio.com/console
auth_token  = "ebf7b7ad1cac85394e1e9fb117ddbdb5"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16033252310", 
    from_="+15168530062",
    body="Hello from Python! -Victoria")

print(message.sid)

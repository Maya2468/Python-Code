from twilio import rest

account_sid = "ACd1e0d5c255c9152cbc9296c858418ddc" # Your Account SID from www.twilio.com/console
auth_token  = "59fc867dad5d1e944455791868a13d7e"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body=" Can we look at computers? I'm super excited!",
    to="+14438139394",    # Replace with your phone number
    from_="+14435683620 ") # Replace with your Twilio number

print(message.sid)

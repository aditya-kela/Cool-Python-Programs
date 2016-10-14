from twilio.rest import TwilioRestClient

account_sid = "AC52382b001e198cfd9766b1e6b9aa3562" # Your Account SID from www.twilio.com/console
auth_token  = "9c0289a0815f956b9ba99769f10aa7a7"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hey!Do u have Molly's number. I like her very much and wanna ask her out.",
    to="+12672537107",    # Replace with your phone number
    from_="+14159037107") # Replace with your Twilio number

print(message.sid)
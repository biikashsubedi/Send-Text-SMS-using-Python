from twilio.rest import Client

account_sid = 'AC9fea1cc56259c5a3b0e856b24bc24ecc'
auth_token = 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12016361951',
    body='Hello, This is Bikash Subedi From Direct Web Message ',
    to='+97798XXXXXXXX'
)

print(message.sid)
from twilio.rest import Client

account_sid = "ACff1ae563f7ce9ce2a9ed6d867616e99a"
auth_token = "bd6ca7634859cb86c22eef027d5734bf"
client = Client(account_sid, auth_token)

message = client.api.account.messages.create(to="+16514684168", from_="+16123248793", body="Hello Alex")

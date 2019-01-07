from twilio.rest import Client

class SendListingNotification:

    def __init__(self):
        account_sid = "ACff1ae563f7ce9ce2a9ed6d867616e99a"
        auth_token = "bd6ca7634859cb86c22eef027d5734bf"
        self.client = Client(account_sid, auth_token)

    def send_message(self, number, message):
        # +16514684168
        self.client.api.account.messages.create(to=number, from_="+16123248793", body=message)

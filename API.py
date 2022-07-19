 #send sms function
#region SMS
import os
from twilio.rest import Client  
def send_sms(text):
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)

    message = client.messages \
                    .create(
                         body=text,
                         from_='+12027598952',
                         to='+972502156752'
                     )

    print(message.sid)
#endregion     

#APi


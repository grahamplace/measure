# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client
import os



def init_client():
    # Your Account Sid and Auth Token from twilio.com/console
    account_sid = os.environ['TWILIO_SID']
    auth_token = os.environ['TWILIO_TOKEN']
    return Client(account_sid, auth_token)

def send_survey():
    client = init_client()

    my_phone_number = os.environ['MY_PHONE']
    twilio_phone_number = os.environ['TWILIO_PHONE']
    survey_link = os.environ['SURVEY_URL']

    sms_string = "Good morning! Please complete today's Measure survey:\n" \
                 f"{survey_link}\n" \
                 "Remember: What gets measured gets managed!"

    message = client.messages.create(
                                  body=sms_string,
                                  from_=twilio_phone_number,
                                  to=my_phone_number
                              )


if __name__ == '__main__':
    send_survey()

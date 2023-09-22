from twilio.rest import Client

# Replace these with your Twilio credentials
account_sid = 'YOUR_ACCOUNT_SID'
auth_token = 'YOUR_AUTH_TOKEN'
twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'
recipient_phone_number = 'RECIPIENT_PHONE_NUMBER'  # Should be in the format: '+1234567890'

# Initialize the Twilio client
client = Client(account_sid, auth_token)

try:
    # Make a phone call
    call = client.calls.create(
        to=recipient_phone_number,
        from_=twilio_phone_number,
        url='http://demo.twilio.com/docs/voice.xml'  # A URL that contains TwiML instructions (e.g., for a greeting)
    )

    print(f"Calling {recipient_phone_number}... Call SID: {call.sid}")
except Exception as e:
    print(f"Error making the phone call: {e}")

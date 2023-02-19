from twilio.rest import Client 
 
account_sid = 'AC69ce5bb960b5fc9921b59cc7159ab247' 
auth_token = 'bacc8cbd7b26c672b8af20dda0b2bf72' 
client = Client(account_sid, auth_token) 

def sendBagSMS(numbers, bagName):
    if len(numbers) > 0:
        response = client.messages.create(
            body='Bag: {} available now, please check your email for the link'.format(bagName), 
            to= numbers,
            messaging_service_sid='MG297cf4f21fd71ea64f0c0683f054cc88',
        )
        print("SMS send to {0}, about bag: {1}".format(numbers, bagName))
    return {
        "body": 'Bag: {} available now, please check your email for the link'.format(bagName),
        "to": ', '.join(numbers)
    }

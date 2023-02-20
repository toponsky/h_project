from twilio.rest import Client 
 
account_sid = 'AC69ce5bb960b5fc9921b59cc7159ab247' 
auth_token = '299a35f34bda366f846d61aea6e1a283' 
client = Client(account_sid, auth_token) 

def sendBagSMS(numbers, bagName):
    try:
        if len(numbers) > 0:
            for number in numbers: 
                response = client.messages.create(
                    body='Bag: {} available now, please check your email for the link'.format(bagName), 
                    to= number,
                    messaging_service_sid='MG297cf4f21fd71ea64f0c0683f054cc88'
                )
            print("SMS send to {0}, about bag: {1}".format(number, bagName))
        return {
            "body": 'Bag: {} available now, please check your email for the link'.format(bagName),
            "to": ', '.join(numbers)
        }
    except:
        print('Something wrong to send test message')
        return {
            "body": 'Something wrong to send test message',
            "to": ', '.join(numbers)
        }
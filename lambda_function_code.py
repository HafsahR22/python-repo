import json
import boto3
import random 

sqs = boto3.client('sqs')
queue_url = 'https://sqs.us-east-1.amazonaws.com/456863550460/customer_orders'

def lambda_handler(event,context): 
    message = str(random.randint(1,10))
    response = sqs.send_message(
    QueueUrl= queue_url,
    MessageBody=message,
    DelaySeconds=2)

    return {
        'statusCode': 200,
        'body': json.dumps(message)
    }
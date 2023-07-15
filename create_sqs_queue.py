import boto3

# This gets the service resource
sqs = boto3.resource('sqs')

# This creates the queue and name
queue = sqs.create_queue(QueueName='customer_orders')

# You can now access the url
print(queue.url)


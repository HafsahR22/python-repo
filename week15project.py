import boto3

# This gets the service resource
sqs = boto3.resource('sqs')

# This creates the queue and returns an SQS.Queue instance
queue = sqs.create_queue(QueueName='week15project')

# You can now access identifiers and attributes
print(queue.url)

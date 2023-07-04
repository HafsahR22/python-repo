import boto3

ec2 = boto3.client('ec2')

response = ec2.describe_instances()
instances = response['Reservations']

for instance in instances:
    instance_id = instance['Instances'][0]['InstanceId']
    state = instance['Instances'][0]['State']['Name']

    if state == 'running':
        response2 = ec2.stop_instances(InstanceIds=[instance_id])
        print(response2)
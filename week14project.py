import boto3


def response(stop_instances): 
    response = client.stop_instances(
    InstanceIds=[
        'i-01f1e91b0ed9d7a14)','i-0f16aa3a2eb2e9c45','i-043faf628c445a688'
    ],
)

print(response)

import time

import schedule

schedule.every(stop_instances).day.at("03:00").do(job,'It is 03:00')

while True:
    schedule.stop_instances()
    time.sleep(60) 

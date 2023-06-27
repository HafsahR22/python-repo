import boto3
import os 

def download_single_object (client, bucket, key, filename):
    client.download_file(bucket, key, filename)
    
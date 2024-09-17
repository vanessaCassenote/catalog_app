import boto3
import pandas as pd
import json

class S3():
    def __init__(self):
        with open('src/config/aws/s3/s3_access.json', 'r') as file:
            s3_access = json.load(file)
        
        self.s3 = boto3.client(
            service_name=s3_access['s3']["service_name"],
            region_name=s3_access['s3']["region_name"],
            aws_access_key_id=s3_access['s3']["aws_access_key_id"],
            aws_secret_access_key=s3_access['s3']["aws_secret_access_key"]
        )
    def access(self):
        return self.s3

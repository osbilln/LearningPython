# coding: utf-8
import boto3
boto3.Session
boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
session = boto3.Session(profile_name='pythonAutomation')
print(session)
s3 = session.resource('s3')
print(s3)
for bucket in s3.buckets.all():
    print(bucke)
new_bucket = s3.create_bucket(Bucket='osbilln-automation-bucket')
new_bucket = s3.create_bucket(Bucket='osbilln-automation-bucket', CreateBucketConfiguration={'LocationConstraint': 'us-east-2')}
new_bucket = s3.create_bucket(Bucket='osbilln-automation-bucket', CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})
for bucket in s3.buckets.all():
    print(bucke)
for bucket in s3.buckets.all():
    print(bucket)
ec2_client = session.client('ec2')
print(ec2_client)
get_ipython().run_line_magic('history', '')
get_ipython().run_line_magic('save', 'ipythonsession.py 1-18')

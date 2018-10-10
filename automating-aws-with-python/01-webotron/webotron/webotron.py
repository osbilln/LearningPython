import boto3
import click
from botocore.exceptions import ClientError

session = boto3.Session(profile_name='pythonAutomation')
s3 = session.resource('s3')
@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

# @click_command('list_buckets')
@cli.command('list_buckets')
def list_buckets():
    "List all s3 buckets"
    for bucket in s3.buckets.all():
        print(bucket)

@cli.command('list-buckets-objects')
@click.argument('bucket')
def list_buckets_objects():
    "List objects in an s3 buckets"
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)
#    pass

@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    "Create and configure S3 bucket"
    s3_bucket = None
    try:
        s3_bucket = s3.create_bucket( 
       	   Bucket=bucket, 
           CreateBucketConfiguration={'LocationConstraint': 'session.region_name'} 
        ) 
    except ClientError as e: 
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedbyYou': 
           s3_bucket = s3.Bucket(bucket)
        else:
           raise e
#    s3_bucket = s3.create_bucket(
#        Bucket='bucket',
#        CreateBucketConfiguration={'LocationConstraint': 'session.region_name'}
#    )
    policy = """
    {
      "Version":"2012-10-17",
      "Statement":[
        {
          "Sid":"AddCannedAcl",
          "Effect":"Allow",
          "Principal": {"AWS": ["arn:aws:iam::111122223333:root","arn:aws:iam::444455556666:root"]},
          "Action":["s3:PutObject","s3:PutObjectAcl"],
          "Resource":["arn:aws:s3:::%s/*"],
          "Condition":{"StringEquals":{"s3:x-amz-acl":["public-read"]}}
        }
      ]
    }
    """ % s3_bucket.name
    policy = policy.strip()

    pol = s3_bucket.Policy()
    pol.put(Policy=policy)
    ws = s3_bucket.Website()
    ws.put(WebsiteConfiguration={
            'ErrorDocument': {
                'Key': 'error.html'
            },
            'IndexDocument': {
                'Suffix': 'index.html'
            }
    })
    url = "http://%s.s3-website-us-east-2.amazonaws.com" % s3_bucket.name
    return
if __name__ == '__main__':
    cli()
# list_buckets

import boto3
import click

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

if __name__ == '__main__':
    cli()
# list_buckets
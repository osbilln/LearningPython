#!/usr/bin/python
# -*-coding: utf-8 -*-


""" webotron: deploy webiste to AWS
webotron automates the process of deploying static websites
- Configure AWS buckets
    - Create them
    - Set them up for static website hosting
    - list buckets
"""


import boto3
import click
from botocore.exceptions import ClientError
from pathlib import Path
import mimetypes
from bucket import BucketManager

session = boto3.Session(profile_name='pythonAutomation')
bucket_manager = BucketManager(session)
#s3 = session.resource('s3')


@click.group()
def cli():
    "Webotron deploys websites to AWS"
    pass

# @click_command('list_buckets')


@cli.command('list-buckets')
def list_buckets():
    """ List all s3 buckets """
    #for bucket in bucket_manager.s3.buckets.all():
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-buckets-objects')
@click.argument('bucket')
def list_buckets_objects():
    """List objects in an s3 buckets"""
#    for obj in s3.Bucket(bucket).objects.all():
    for obj in s3.Bucket(bucket).objects.all():
        print(obj)
#    pass


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """ Create and configure S3 bucket """
    s3_bucket = None
    try:
        s3_bucket = s3.create_bucket(
            Bucket=bucket,
            CreateBucketConfiguration=
            {'LocationConstraint': session.region_name}
        )
    except ClientError as e:
        if e.response['Error']['Code'] == 'BucketAlreadyOwnedbyYou':
            s3_bucket = s3.Bucket(bucket)
        else:
            raise e
    policy = """
    {
      "Version":"2012-10-17",
      "Statement":[
        {
          "Sid":"AddCannedAcl",
          "Effect":"Allow",
          "Principal": {"AWS": \
          ["arn:aws:iam::111122223333:root","arn:aws:iam::444455556666:root"]},
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


def upload_file(self, bucket, path, key):
        """Upload path to s3_bucket at key."""
        content_type = mimetypes.guess_type(key)[0] or 'text/plain'

        etag = self.gen_etag(path)
        if self.manifest.get(key, '') == etag:
            return

        return bucket.upload_file(
            path,
            key,
            ExtraArgs={
                'ContentType': content_type
            },
            Config=self.transfer_config
        )

@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')

def sync(self, pathname, bucket_name):
        """Sync contents of path to bucket."""
        bucket = self.s3.Bucket(bucket_name)
        self.load_manifest(bucket)

        root = Path(pathname).expanduser().resolve()

        def handle_directory(target):
            for p in target.iterdir():
                if p.is_dir():
                    handle_directory(p)
                if p.is_file():
                    self.upload_file(bucket, str(p), str(p.relative_to(root)))

        handle_directory(root)
if __name__ == '__main__':
    cli()
# list_buckets
""" EOF """

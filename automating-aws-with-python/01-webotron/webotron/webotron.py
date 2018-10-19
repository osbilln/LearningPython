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

from bucket import BucketManager
from botocore.exceptions import ClientError
from pathlib import Path
import mimetypes

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
def list_buckets_objects(bucket):
    """List objects in an s3 buckets"""
    for obj in bucket_manager(bucket).all_objects(obj):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """ Create and configure S3 bucket """
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)
    bucket_manager.configure_website(s3s3_bucket)

    return


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of PATHNAME to bucket."""
    bucket_manager.sync(pathname, bucket)
    print(bucket_manager.get_bucket_url(bucket_manager.s3.Bucket(bucket))


if __name__ == '__main__':
    cli()

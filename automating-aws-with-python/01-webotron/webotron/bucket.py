# -*- coding: utf-8 -*-

""" Classes forS3 Buckets. """

class BucketManager:
    """Manage an S3 Bucket."""
    def __init__(self, session):
        """Create a BucketManager object."""
        self.s3 = session.resource('s3')

    def all_buckets(self):
        """Create a BuvketManager object."""
        self.s3 = session.resource('s3')

    def all_objects(self, bucket):
        return self.s3.Bucket(bucket).objects.all()

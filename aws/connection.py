"""
Class to represent Boto 3 session connectivity
"""
from builtins import object
from builtins import str
import logging
import boto3
from botocore.exceptions import ClientError, BotoCoreError, EndpointConnectionError


class Connection(object):
    def __init__(self, region, service):
        """
        Connection constructor
        """
        self.region = region
        self.validate_service(service)
        self.service = service

    def session_setup(self):
        """
        Create and return session to AWS API based on profile and region
        """
        try:
            session = boto3.session.Session(region_name=self.region)
        except (BotoCoreError, EndpointConnectionError, ClientError) as e:
            logging.exception(e)
            return None
        return session

    def resource_connection(self):
        """
        Create and return Resource Connection based on service type
        e.g ec2, s3, dynamodb
        """
        session = self.session_setup()
        try:
            conn = session.resource(self.service)
        except (ValueError, ClientError, BotoCoreError) as e:
            logging.exception(e)
            return None
        return conn

    def client_connection(self):
        """
        Create and return Client Connection based on service type
        e.g ec2, s3, dynamodb
        """
        session = self.session_setup()
        try:
            conn = session.client(self.service)
        except (ValueError, ClientError, BotoCoreError) as e:
            logging.exception(e)
            return None
        return conn

    def validate_service(self, service):
        """
        Validation method for the service attribute
        to ensure it corresponds to value equal to ec2
        """
        try:
            if service.lower() not in ['ec2', 'autoscaling', 'logs']:
                raise ValueError('Ensure you enter valid AWS services i.e ec2, logs, s3')
        except ValueError as e:
            exit(str(e))

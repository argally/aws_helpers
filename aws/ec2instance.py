"""
Class to represent EC2 instance resources
"""
from __future__ import print_function
from builtins import str
from builtins import object
from aws.connection import Connection
import pandas as pd


class EC2Instance(object):
    """
    Working with EC2 instances
    """

    def __init__(self, region, profile, service):
        """
        EC2Instance Constructor which instanciates Connection class
        """
        self.region = region
        self.profile = profile
        self.validate_service(service)
        self.service = service
        self.conn = Connection(region, profile, service)

    def validate_service(self, service):
        """
        Validation method for the service attribute
        to ensure it corresponds to value equal to ec2
        """
        try:
            if service.lower() != "ec2":
                raise ValueError('For EC2 instances ensure attribue service equals ec2')
        except ValueError as e:
            exit(str(e))

    def ec2_instance_dump_filter(self):
        """
        Perform the initial connection to EC2 using the Connection class
        """
    #   ec2 = conn.resource('ec2')
        connect = self.conn.ec2_resource_connection()
        filters = [
                {
                    'Name': 'instance-state-name',
                    'Values': ['running']
                }
        ]
        instance_count = 0
        instances = connect.instances.filter(Filters=filters)
        for instance in instances:
            # for each instance, append to array and print instance id()
            print(
                "Id: {0}\nPlatform: {1}\nType: {2}\nPublic IPv4: {3}\nAMI: {4}\nState: {5}\n".format(
                    instance.id, instance.platform, instance.instance_type, 
                    instance.public_ip_address, instance.image.id, instance.state
                )
            )
            instance_count += 1

        print('Number of Instances found %s ' % instance_count)

    def ec2_instance_count_resource(self):
        """
        Perform the initial connection to EC2 using the Resource Connection class
        """
        connect = self.conn.resource_connection()
        instance_count = 0
        d = []
        instances = connect.instances.all()
        for instance in instances:
            instance_count += 1
            for tags in instance.tags:
                if tags["Key"] == 'Name':
                    instancename = tags["Value"]
            d.extend([(instancename, instance.id, instance.image_id, instance.state['Name'],
            instance.private_ip_address)])
        print('Number of Instances found %s ' % instance_count)
        df = pd.DataFrame(d, columns=["Name", "Id", "Image", "State", "Private_IP"])
        df.set_index('Id', drop=True, inplace=True)
        return df.sort_values(by='Name')

    def ec2_instance_count_client(self):
        """
        Perform the initial connection to EC2 using the Client Connection class
        """
        connect = self.conn.client_connection()
        instance_count = 0
        instances = connect.describe_instances()
        for reservation in instances["Reservations"]:
            for instance in reservation["Instances"]:
                # This sample print will output entire Dictionary object
                # print(instance)
                # This will print will output the value of the Dictionary key 'InstanceId'
                print(instance["InstanceId"])
                instance_count += 1
        print('Number of Instances found %s ' % instance_count)

"""
Class to represent EC2 EIP resources
"""
from __future__ import print_function
from builtins import str
from builtins import object
import pandas as pd


class EC2Eip(object):
    """
    Working with EC2 Elastic IP
    """

    def __init__(self):
        """
        EC2Eip Constructor which instanciates Connection class
        """

    def ec2_eip_count(self, eipdict):
        """
        Perform the total count on artifacts found
        """
        eip_count = 0
        for eip in eipdict:
            eip_count += 1
        return eip_count

    def ec2_eip_count_client(self, conn):
        """
        Perform the initial connection to EC2 Session
        """
        eip_list_dict = []
        filters = [
            {'Name': 'domain', 'Values': ['vpc']}
        ]
        eips = conn.describe_addresses(Filters=filters)
        for eip_dict in eips['Addresses']:
            eip_tagged_name = ""
            eip_tagged_az = ""
            eip_tagged_stack = ""
            try:
                for eip_tags in eip_dict['Tags']:
                    if 'Name' in eip_tags["Key"]:
                        eip_tagged_name = eip_tags["Value"]
                    elif 'AZ' in eip_tags["Key"]:
                        eip_tagged_az = eip_tags["Value"]
                    elif 'Stack' in eip_tags["Key"]:
                        eip_tagged_stack = eip_tags["Value"]
            except KeyError:
                eip_tagged_name = ""
                eip_tagged_az = ""
                eip_tagged_stack = ""
            try:
                eip_assoc_id = eip_dict['AssociationId']
            except KeyError:
                eip_assoc_id = ""
            try:
                eip_instance_id = eip_dict['InstanceId']
            except KeyError:
                eip_instance_id = ""
            try:
                eip_eni_id = eip_dict['NetworkInterfaceId']
            except KeyError:
                eip_eni_id = ""
            try:
                private_ip = eip_dict['PrivateIpAddress']
            except KeyError:
                private_ip = ""
            eip_list_dict.extend([(eip_tagged_name, eip_tagged_az, eip_tagged_stack, 
                eip_dict['PublicIp'], eip_dict['AllocationId'], eip_assoc_id, eip_instance_id, eip_eni_id, private_ip)])
        eip_count = self.ec2_eip_count(eip_list_dict)
        print('Number of Eip found %s ' % eip_count)
        df = pd.DataFrame(eip_list_dict, columns=["Name", "AZ", "Stack", "EIP", "AllocId", "AssocId", "InstanceId", "NetworkInterfaceId", "PrivateIpAddress"])
        df.set_index('AllocId', drop=True, inplace=True)
        return df.sort_values(by='Name')
    

    def ec2_eip_instance_client(self,):
        """
        Perform the initial connection to EC2 using the Client Connection class
        """
        connect = self.conn.client_connection()
        eip_count = 0
        d = []
        filters = [
            {'Name': 'domain', 'Values': ['vpc']}
        ]
        eips = connect.describe_addresses(Filters=filters)
        for eip_dict in eips['Addresses']:
            eip_count += 1
            try:
                instanceid = eip_dict['InstanceId']
                return instanceid
            except KeyError:
                pass

"""
Class to represent EC2 instance resources
"""
from __future__ import print_function
from builtins import str
from builtins import object
from aws.connection import Connection
import pandas as pd


class AutoScaleInstanceCount(object):
    """
    Working with EC2 Autoscale groups
    """

    def __init__(self, tags):
        """
        EC2Eip Constructor which instanciates Connection class
        """
        self.tags = tags

    def autoscale_count(self, resourceconn, clientconn):
        """
        Perform the initial connection to EC2 Session
        """
        asg_inst_list = []
        paginator = clientconn.get_paginator('describe_auto_scaling_groups')
        page_iterator = paginator.paginate(
            PaginationConfig={'PageSize': 100}
        )
        filtered_asgs = page_iterator.search(
            'AutoScalingGroups[] | [?contains(Tags[?Key==`{}`].Value, `{}`)]'.format(
                'NODEROLE', self.tags)
        )
        for asg in filtered_asgs:
            print(asg['AutoScalingGroupName'])
            instance_ids = [i for i in asg['Instances']]
            for instance in instance_ids:
                id=(instance['InstanceId'])
                instance = resourceconn.Instance(id)
                print(
                "Id: {0}\nIP: {1}\n".format(
                    instance.id, instance.private_ip_address
                )
            )
           
    

   


from __future__ import absolute_import
from __future__ import print_function
from aws.connection import Connection
from aws.ec2instance import EC2Instance
from aws.ec2elasticip import EC2Eip
from tabulate import tabulate

myconn = Connection('ca-central-1', 'ec2')
client_conn = myconn.client_connection()

eip_table = EC2Eip()
e2_table = eip_table.ec2_eip_count_client(client_conn)

#e2_table = (ec2.ec2_instance_count_resource())
#print(tabulate(e2_table, headers=e2_table.columns, tablefmt="jira"))
# print(e2_table)
# print(e2_table['Name'])

#e2_table = ec2.ec2_eip_count_client()
#print(e2_table)

print(tabulate(e2_table, headers=e2_table.columns, tablefmt="grid"))
#print(e2_table)

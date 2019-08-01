import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.filter(Filters=[
{
	'Name': 'availability-zone',
	'Values': ['us-east-2b']
},
{
	'Name': 'instance-state-name',
	'Values': ['running']
}
	]):

    tags = instance.create_tags(Tags=[{'Key':'Backup', 'Value':'Yes'}]) 
    print('Instance id is {} and instance type is {} and its tag {}'.format(instance.instance_id, instance.instance_type, instance.tags))

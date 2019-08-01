import boto3

session = boto3.session.Session(region_name='us-west-2')

ec2 = session.resource('ec2')

for instance in ec2.instances.filter(Filters=[
{
	'Name': 'tag:NODEROLE',
	'Values': ['general']
},
{
	'Name': 'tag:Name',
	'Values': ['devtestcigeneral']
},
{
	'Name': 'instance-state-name',
	'Values': ['running']
}
	]):

#    tags = instance.create_tags(Tags=[{'Key':'Backup', 'Value':'Yes'}])
    print('**** NODEROLE=general *****')
    for tags in instance.tags:
    	if tags["Key"] == 'Name':
    		name = tags["Value"]
    print('Instance id is {} and instance type is {} and its tag {}'.format(instance.instance_id, instance.instance_type, name ))
    if name == 'devtestcigeneral':
    	tags = instance.create_tags(Tags=[{'Key':'NODEROLE', 'Value':'not_general'}])
   

for instance in ec2.instances.filter(Filters=[
{
	'Name': 'tag:NODEROLE',
	'Values': ['ingress']
},
{
	'Name': 'tag:Name',
	'Values': ['devtestciingress']
},
{
	'Name': 'instance-state-name',
	'Values': ['running']
}
	]):

#    tags = instance.create_tags(Tags=[{'Key':'Backup', 'Value':'Yes'}])
    print('**** NODEROLE=ingress *****')
    for tags in instance.tags:
    	if tags["Key"] == 'Name':
    		name = tags["Value"]
    print('Instance id is {} and instance type is {} and its tag {}'.format(instance.instance_id, instance.instance_type, name ))
    if name == 'devtestciingress':
    	tags = instance.create_tags(Tags=[{'Key':'NODEROLE', 'Value':'not_ingress'}])
   
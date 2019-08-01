import boto3

ec2 = boto3.resource('ec2')

ec2.instances.filter(Filters=[
{
	'Name': 'availability-zone',
	'Values': ['us-east-2b']
},
{
	'Name': 'instance-state-name',
	'Values': ['running']
}
	]).stop()
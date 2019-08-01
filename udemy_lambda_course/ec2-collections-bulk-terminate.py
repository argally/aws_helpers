import boto3

ec2 = boto3.resource('ec2')

for instance in ec2.instances.filter(Filters=[
{
	'Name': 'availability-zone',
	'Values': ['us-east-2b']
},
{
	'Name': 'instance-state-name',
	'Values': ['stopped']
}
	]):
    
    response = instance.terminate(
)

    print('Instance id is {} and instance state is {}'.format(instance.instance_id, instance.state))

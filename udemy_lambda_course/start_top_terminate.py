import boto3

client = boto3.client('ec2')

resp = client.terminate_instances(InstanceIds=['i-0be98e0deceb5fd30'])

for instances in resp['TerminatingInstances']:
	print("The instance id terminated {}".format(instances['InstanceId']))
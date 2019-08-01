import boto3

client = boto3.client('ec2')
resp = client.run_instances(ImageId = 'ami-0c55b159cbfafe1f0',
					 InstanceType = 't2.micro',
					 Placement={
					 'AvailabilityZone': 'us-east-2b'
					 },
					 MinCount = 1,
					 MaxCount = 1)

for instance in resp['Instances']:
	print(instance['InstanceId'])
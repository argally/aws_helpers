import boto3

session = boto3.session.Session(region_name='eu-west-1')

client = session.client('ec2')

resp = client.describe_instances(
     Filters=[
        {
            'Name': 'instance-state-name',
            'Values': [
                'running',
            ]
        },
    ],
	)

for reservation in resp['Reservations']:
	for instance in reservation['Instances']:
		print("Instance is {}". format(instance['InstanceId']))


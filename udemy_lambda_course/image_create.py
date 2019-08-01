import boto3 

#########
# Create images
########

source_region = 'us-east-2'
ec2 = boto3.resource('ec2', region_name=source_region)

instances = ec2.instances.filter(InstanceIds = ['i-0bb6ed56d501218bd'])

image_ids = []

for instance in instances:
	image = instance.create_image(Name = 'Demo boto - ' + instance.id, Description = 'Demo boto' + instance.id)
	image_ids.append(image.id)

print("Images {} being created in  {}".format(image_ids, source_region))


#######
# Wait for images to be available
######

client = boto3.client('ec2', region_name = source_region)

waiter = client.get_waiter('image_available')

waiter.wait(Filters=[{

	'Name': 'image-id',
	'Values': image_ids

	}])	

print("Images available {} in region {}".format(image_ids, source_region))

#######
# copy image to other region
######

destination_region = 'ap-south-1'

client = boto3.client('ec2', region_name = destination_region)

for image_id in image_ids:
	client.copy_image(Name='Boto3 Copy '+image_id, SourceImageId=image_id, SourceRegion=source_region)

print("Images {} being copied to  {}".format(image_ids, destination_region))

#######
# Wait for images to be available
######

client = boto3.client('ec2', region_name = destination_region)

waiter = client.get_waiter('image_available')

waiter.wait(Filters=[{

	'Name': 'image-id',
	'Values': image_ids

	}])	

print("Images available {} in region {}".format(image_ids, destination_region))
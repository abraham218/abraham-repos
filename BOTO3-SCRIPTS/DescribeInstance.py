import boto3
from pprint import pprint
aws_con=boto3.session.Session()
client = aws_con.client(service_name='ec2')
response = client.describe_instances()
for each in response['Reservations']:
    for each_instance in each['Instances']:
        #print(each_instance)
        print("###########################################################")
        instance_id = each_instance['InstanceId']
        image_id = each_instance['ImageId']
        Instant_type = each_instance['InstanceType']
        IP = each_instance['PrivateIpAddress']
        print(f"image : {image_id} instance : {instance_id} Instant_type : {Instant_type} IP : {IP}")
for oneach in response['Reservations']:
	for item in oneach['Instances']:
		status = item['State']
		print(f"Instance-state : {status['Name']}")


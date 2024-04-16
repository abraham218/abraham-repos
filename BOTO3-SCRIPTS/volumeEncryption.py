import boto3
from pprint import pprint
aws_mang=boto3.session.Session()
ec2_con=aws_mang.client(service_name='ec2',region_name='us-west-1')
resp = ec2_con.describe_instances()['Reservations']
for each in resp:
	for item in each['Instances']:
		#pprint(item)
		IP = item['PrivateIpAddress']
		VPCID = item['VpcId']
		for sg in item['SecurityGroups']:
			SG_Name = sg['GroupId']
		print(f"EC2 info\nIP: {IP} ,VpcId: {VPCID}, SG: {SG_Name}")
		print('###################################################################################')
###  VOL #####
aws_mang1 = boto3.session.Session()
ec2_vol = aws_mang1.client('ec2')
res  = ec2_vol.describe_volumes()['Volumes']
for each_item in res:
	#pprint(each_item)
	#print(each_item['State'])
	print("The Volume Encyrption: {}\nSnapshotID: {}\nVolumeType: {}".format(each_item['Encrypted'], each_item['SnapshotId'], each_item['VolumeType']))

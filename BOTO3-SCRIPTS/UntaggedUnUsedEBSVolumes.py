import boto3
from pprint import pprint

aws_con=boto3.session.Session() # profile_name='default'
ec2_res=aws_con.resource(service_name='ec2', region_name='us-west-1')

for each in ec2_res.volumes.all():
	volumeStatus = each.state
	print("volumeStatus: {}\nVolumeID: {}".format([each.state], [each.id]))
import boto3
import sys

aws_con=boto3.session.Session()
ec2_con=aws_con.client(service_name='ec2',region_name='us-west-1')

while True:
	print("The Script Performs Start/Stop/Terminate")
	print("""
	1. start
	2. stop
	3. terminate
	4. Exit 	""")
	opt=int(input("Enter the Options : "))
	if opt==1:
		print("Start Ec2")
		instance_ID = input("Enter Instance ID")
	elif opt==2:
		print("stop Ec2")
		instance_ID = input("Enter Instance ID")
	elif opt==3:
		print("terminate Ec2")
		instance_ID = input("Enter Instance ID")
	elif opt==4:
		print("Exit")
		sys.exit()
	else:
		print("Invalid Options")
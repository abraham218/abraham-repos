import boto3
from pprint import pprint

session=boto3.session.Session()
ec2_client=session.client(service_name='ec2', region_name='us-west-1')
all_regions=[]
for each in ec2_client.describe_regions()['Regions']:
	all_regions.append(each.get('RegionName'))
	#ec2_client=session.client(service_name='ec2', region_name='all_regions')
#####################################
#### MFA  ##################

# Initialize the Boto3 client for IAM
iam_client = boto3.client('iam')

# List all IAM users
response = iam_client.list_users()

# Iterate through each user
for user in response['Users']:
    user_name = user['UserName']
    
    # Check if the user has MFA devices configured
    mfa_response = iam_client.list_mfa_devices(UserName=user_name)
    mfa_devices = mfa_response['MFADevices']
    
    if mfa_devices:
        print(f"IAM user '{user_name}' is using MFA devices.")
    else:
        print(f"IAM user '{user_name}' is not using MFA devices.")


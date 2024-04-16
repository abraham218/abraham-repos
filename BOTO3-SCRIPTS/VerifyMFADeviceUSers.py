import boto3
from pprint import pprint

session=boto3.session.Session()
iam_con=session.client('iam')

list_users=iam_con.list_users()['Users']
for each in list_users:
	user_name = each.get('UserName')
	mfa_device = iam_con.list_mfa_devices(UserName=user_name)
	mfa_resp = mfa_device['MFADevices']
	if mfa_resp:
		print(f"IAM user '{user_name}' is using MFA devices.")
	else:
		print(f"IAM user '{user_name}' is not using MFA devices.")


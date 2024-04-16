import boto3
aws_con=boto3.session.Session()
iam_con=aws_con.resource('iam')
resp = iam_con.virtual_mfa_devices.filter(AssignmentStatus='Any')
#print(dir(resp))
print(resp.all())




for ab in iam_con.virtual_mfa_devices.all():
	#print(dir(ab))
	print(ab.serial_number)


# for each in iam_con.users.all():
# 	print(each.policies)
# 	print("#################################################################################")
# 	#print(dir(each))

# for item in iam_con.roles.all():
# 	#print(dir(item))
# 	#print(item.policies)
# 	print(item.role_name)

# for ab in iam_con.policies.all():
# 	print(ab)
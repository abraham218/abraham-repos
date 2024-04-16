import boto3
aws_con=boto3.session.Session()
ec2_con=aws_con.client('ec2')

resp = ec2_con.run_instances(ImageId='ami-0b990d3cfca306617', MinCount=1, MaxCount=1, InstanceType='t2.micro')
for instance in resp['Instances']:
    print(instance['InstanceId'])
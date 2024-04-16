import boto3
aws_con = boto3.session.Session()
iam_con = aws_con.resource(service_name='iam')
s3_con = aws_con.resource('s3')

def ListIamUsers():
    for each_user in iam_con.users.all():
        print(f"Iam User : {each_user.name}")

def ListS3():
    for each_bucket in s3_con.buckets.all():
        print(each_bucket)

if __name__ == "__main__":
    ListIamUsers()
    ListS3()


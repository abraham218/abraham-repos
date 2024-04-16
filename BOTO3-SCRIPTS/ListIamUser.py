# listing IAM Client Objects

import boto3

aws_con=boto3.session.Session()
iam_con_cli=aws_con.client('iam')
#print(iam_con_cli.list_users())
for each in iam_con_cli.list_users()['Users']:
    
    print("############################################################################")
    retry_attempts = (iam_con_cli.list_users()['ResponseMetadata']['RetryAttempts'])
    print(f"Name : {each['UserName']}  : {each['Arn']} Retry-Attempts : {retry_attempts}")
    print("############################################################################")
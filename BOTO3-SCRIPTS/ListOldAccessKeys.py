import boto3
from datetime import datetime, timedelta

def list_users_with_old_access_keys():
    # Create an IAM client
    iam = boto3.client('iam')

    # List all IAM users
    users = iam.list_users()['Users']

    # Get the current date
    current_date = datetime.now()

    # List to store users with old access keys
    users_with_old_access_keys = []

    # Iterate through users
    for user in users:
        # Get the access keys for the user
        access_keys = iam.list_access_keys(UserName=user['UserName'])['AccessKeyMetadata']
        for key in access_keys:
            # Calculate the age of the access key
            create_date = key['CreateDate']
            age = current_date - create_date.replace(tzinfo=None)

            # Check if the access key is more than a year old
            if age > timedelta(days=365):
                users_with_old_access_keys.append(user['UserName'])
                break  # Move to the next user

    return users_with_old_access_keys

# List users with old access keys
old_access_key_users = list_users_with_old_access_keys()
print("Users with Old Access Keys (More than a year old):")
for user in old_access_key_users:
    print(user)

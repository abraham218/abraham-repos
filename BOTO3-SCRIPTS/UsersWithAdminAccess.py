import boto3

def list_users_with_admin_access():
    # Create an IAM client
    iam = boto3.client('iam')

    # List all IAM users
    users = iam.list_users()['Users']

    # List to store users with admin access
    admin_users = []

    # Iterate through users
    for user in users:
        # Get list of attached policies for the user
        attached_policies = iam.list_attached_user_policies(UserName=user['UserName'])['AttachedPolicies']
        for policy in attached_policies:
            # Check if policy is AdministratorAccess
            if policy['PolicyName'] == 'AdministratorAccess':
                admin_users.append(user['UserName'])
                break

        # Get list of groups the user belongs to
        user_groups = iam.list_groups_for_user(UserName=user['UserName'])['Groups']
        for group in user_groups:
            # Get list of attached policies for the group
            group_policies = iam.list_attached_group_policies(GroupName=group['GroupName'])['AttachedPolicies']
            for policy in group_policies:
                # Check if policy is AdministratorAccess
                if policy['PolicyName'] == 'AdministratorAccess':
                    admin_users.append(user['UserName'])
                    break

    return admin_users

# List all IAM users with admin access
admin_users = list_users_with_admin_access()
print("Users with Admin Access:")
for user in admin_users:
    print(user)

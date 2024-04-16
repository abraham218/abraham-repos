import boto3

def list_roles_with_admin_access():
    # Create an IAM client
    iam = boto3.client('iam')

    # Get all IAM roles
    roles = iam.list_roles()['Roles']

    # List to store roles with admin access
    admin_roles = []

    # Iterate through roles
    for role in roles:
        # Get policy attached to the role
        attached_policies = iam.list_attached_role_policies(RoleName=role['RoleName'])['AttachedPolicies']
        for policy in attached_policies:
            # Check if policy is AdministratorAccess
            if policy['PolicyName'] == 'AdministratorAccess':
                admin_roles.append(role['RoleName'])
                break

    return admin_roles

# List all roles with admin access
admin_roles = list_roles_with_admin_access()
print("Roles with Admin Access:")
for role in admin_roles:
    print(role)


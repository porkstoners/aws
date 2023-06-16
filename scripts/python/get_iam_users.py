import boto3
from tabulate import tabulate

# Create IAM client
iam_client = boto3.client('iam')

# List all IAM users
response = iam_client.list_users()

# Process user data
users = response['Users']

# Prepare data for tabulate
table_data = []
for user in users:
    username = user['UserName']
    
    # Get group memberships for the user
    response = iam_client.list_groups_for_user(UserName=username)
    groups = response['Groups']
    
    # Add user and group data to the table
    for group in groups:
        group_name = group['GroupName']
        table_data.append([username, group_name])

# Define table headers
headers = ['IAM User', 'Group Memberships']

# Print table
print(tabulate(table_data, headers=headers, tablefmt='grid'))
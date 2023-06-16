import boto3
from tabulate import tabulate

# Create EC2 client
ec2_client = boto3.client('ec2')

# Retrieve EBS volume information
response = ec2_client.describe_volumes()

# Process volume data
volumes = []
for volume in response['Volumes']:
    volume_id = volume['VolumeId']
    volume_type = volume['VolumeType']
    volume_size = volume['Size']
    attachments = volume['Attachments']

    # Get attached instances
    attached_instances = []
    for attachment in attachments:
        instance_id = attachment['InstanceId']

        # Retrieve instance information
        instance_response = ec2_client.describe_instances(InstanceIds=[instance_id])
        instance_data = instance_response['Reservations'][0]['Instances'][0]
        instance_name = ''
        if 'Tags' in instance_data:
            for tag in instance_data['Tags']:
                if tag['Key'] == 'Name':
                    instance_name = tag['Value']
                    break

        attached_instances.append(f'{instance_id} ({instance_name})')

    volumes.append([
        volume_id,
        volume_type,
        volume_size,
        ', '.join(attached_instances)
    ])

# Print volume table
header = ['Volume ID', 'Volume Type', 'Size (GB)', 'Attached Instances']
table = tabulate(volumes, headers=header, tablefmt='pretty')
print(table)

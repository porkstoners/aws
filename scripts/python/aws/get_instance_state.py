import boto3
from tabulate import tabulate

# Create EC2 client
ec2_client = boto3.client('ec2')

# Retrieve instance information
response = ec2_client.describe_instances()

# Process instance data
instances = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        instance_id = instance['InstanceId']
        instance_type = instance['InstanceType']
        availability_zone = instance['Placement']['AvailabilityZone']
        launch_time = instance['LaunchTime'].strftime('%Y-%m-%d %H:%M:%S')


        # Get private IP address
        private_ip = ''
        if 'PrivateIpAddress' in instance:
            private_ip = instance['PrivateIpAddress']
        else:
            private_ip = 'None'
            
        # Get public IP address
        public_ip = ''
        if 'PublicIpAddress' in instance:
            public_ip = instance['PublicIpAddress']
        else:
            public_ip = 'None'

        # Get AMI ID
        ami_id = instance['ImageId']

        # Check instance state
        state = instance['State']['Name']
        running_state = 'Running' if state == 'running' else 'Not Running'

        # Check if 'Project' tag exists
        project = ''
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key'] == 'Project':
                    project = tag['Value']
                    break
        name = ''
        if 'Tags' in instance:
            for tag in instance['Tags']:
                if tag['Key'] == 'Name':
                    name = tag['Value']
                    break

        
        instances.append([
            name,
            ami_id,
            instance_id,
            instance_type,
            availability_zone,
            launch_time,
            running_state,
            private_ip,
            public_ip,
            project
        ])

# Print instance table
header = ['name', 'ami_id', 'Instance ID', 'Instance Type', 'Availability Zone', 'Launch Time', 'State','private_ip', 'public_ip', 'Project']
table = tabulate(instances, headers=header, tablefmt='pretty')
print(table)

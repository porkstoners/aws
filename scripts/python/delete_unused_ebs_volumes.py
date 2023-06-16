import boto3

# Create EC2 client
ec2_client = boto3.client('ec2')

# Retrieve all EBS volumes
response = ec2_client.describe_volumes()

# Process volume data
unused_volumes = []
for volume in response['Volumes']:
    volume_id = volume['VolumeId']
    attachments = volume['Attachments']

    # Check if volume is not attached to any instance
    if len(attachments) == 0:
        unused_volumes.append(volume_id)

# Delete unused volumes
if len(unused_volumes) > 0:
    print(f"Found {len(unused_volumes)} unused volumes:")
    for volume_id in unused_volumes:
        print(f"- {volume_id}")
    
    confirm = input("Do you want to delete these volumes? (yes/no): ")
    if confirm.lower() == 'yes':
        for volume_id in unused_volumes:
            try:
                ec2_client.delete_volume(VolumeId=volume_id)
                print(f"Deleted volume {volume_id}")
            except Exception as e:
                print(f"Error deleting volume {volume_id}: {str(e)}")
    else:
        print("Aborted. No volumes deleted.")
else:
    print("No unused volumes found.")
import boto3

# AWS credentials and region
aws_access_key_id = 'YOUR_ACCESS_KEY_ID'
aws_secret_access_key = 'YOUR_SECRET_ACCESS_KEY'
aws_region = 'YOUR_REGION'

# EC2 instance details
ami_id = 'AMI_ID'
instance_type = 't2.micro'
key_name = 'YOUR_KEY_PAIR_NAME'
security_group_ids = ['YOUR_SECURITY_GROUP_ID']

# Create EC2 client
ec2_client = boto3.client('ec2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name=aws_region)

# Launch EC2 instance
response = ec2_client.run_instances(
    ImageId=ami_id,
    InstanceType=instance_type,
    KeyName=key_name,
    SecurityGroupIds=security_group_ids,
    MinCount=1,
    MaxCount=1
)

# Get instance ID from the response
instance_id = response['Instances'][0]['InstanceId']

print(f"EC2 instance {instance_id} is being created.")

# Wait for the instance to be in the 'running' state
ec2_client.get_waiter('instance_running').wait(InstanceIds=[instance_id])

print(f"EC2 instance {instance_id} is now running.")

# You can add additional configuration or actions here as needed
# For example, you may want to associate an Elastic IP, attach EBS volumes, etc.

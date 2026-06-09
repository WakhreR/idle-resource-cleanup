# src/lambda_function.py

import boto3

def lambda_handler(event, context):

    ec2 = boto3.client('ec2')

    volumes = ec2.describe_volumes(
        Filters=[
            {
                'Name': 'status',
                'Values': ['available']
            }
        ]
    )

    idle_volumes = []

    for volume in volumes['Volumes']:
        idle_volumes.append(volume['VolumeId'])

    print("Idle Volumes:")
    print(idle_volumes)

    return {
        "statusCode": 200,
        "idle_volumes": idle_volumes
    }

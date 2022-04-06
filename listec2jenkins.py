import boto3
import sys

region=sys.argv[1]
access_key=sys.argv[2]
secret_key=sys.argv[3]

listec2 = boto3.client('ec2',region_name=region,
	aws_access_key_id=access_key,
	aws_secret_access_key=secret_key)

listec2 = listec2.describe_instances()
for printins in listec2['Reservations']:
	for printid in printins['Instances']
	print(printid['ImageId'],
	      printid['InstanceId'],
	      printid['InstanceType'],
	      printid['LaunchTime'],
	      printid['State']['Name'])

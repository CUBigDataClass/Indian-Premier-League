import boto3
import json
from time import sleep

dynamo_db = boto3.resource('dynamodb',
                           aws_access_key_id='...',
                           aws_secret_access_key='...',
                           aws_session_token= '...',
                           region_name= 'us-east-1')

table = dynamo_db.Table('deliveries')

with open('../deliveries.json') as json_file:
    data = json.load(json_file)

count = 0

for key in data:
    if (count % 240 == 0):
        print(count, ' items done')
        sleep(60)
    # if (count > 149800):
    table.put_item(Item= data[key])
    count += 1


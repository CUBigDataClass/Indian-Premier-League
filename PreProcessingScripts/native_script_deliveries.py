import boto3
import json

dynamo_db = boto3.resource('dynamodb',
                           aws_access_key_id='ASIAZDXTUI3TWYNUWBC5',
                           aws_secret_access_key='/lXPIMTiu39F9bWKigM2Gm0yelAO2+8HBpvq3LGy',
                           aws_session_token= 'FwoGZXIvYXdzEJP//////////wEaDCArr02mH3ISsSIqRiLEARLAhLtm37FtC0XhXMS3AzwxbL81t/udWnJGFbuF4Q6Ml5HNX8lNXS44EFajYO+UHEc4oEmJdpZHBHQxY3HZDC46p4gClTDn2o+uo9lVtW57vFwTiXQ5jp1dULeDO0YXpWZzxTiwf08a9/my/VoQtPEbVH5MGsD5GxxFiL6j5MR0+qc/hdDKi4QnRXbYozH0VmsH4lQKdtv024N0x6iVaSnphN8r5gK+32m9tvw4mKHBIPuQPDVGVK27sZf8cDUDcov0HloohKvu8wUyLf4Cl3k3g6KjOVHu81Hdl6JZNAL+dqompu0HNwztNUrbXqzATH/cVO7UvImSOA==',
                           region_name= 'us-east-1')

table = dynamo_db.Table('deliveries')

with open('../deliveries.json') as json_file:
    data = json.load(json_file)

count = 0

for key in data:
    if (count % 100 == 0):
        print(count, ' items done')
    # if (count > 149800):
    table.put_item(Item= data[key])
    count += 1


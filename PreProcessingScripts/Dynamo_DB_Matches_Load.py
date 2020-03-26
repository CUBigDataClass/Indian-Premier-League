import boto3
import csv
import time
import json
dynamodb = boto3.resource('dynamodb',aws_access_key_id='**********',aws_secret_access_key='****************',
                        aws_session_token='*************************'
                        ,region_name='us-east-1')
jsonfile='D:\CUB\Spring20\BigDataArchitecture\Project\matches.json'
dynamoTable=dynamodb.Table('matches')
with open(jsonfile,'r') as jf:
    data=json.load(jf)
# print(data)
# with dynamoTable.batch_writer() as batch:
#     for row in data:
#         for key,value in list(row.items()):
#             if value is None or not value:
#                 row.pop(key)
#         batch.put_item(Item=row)
count=1
for row in data:
    for key,value in list(row.items()):
        if value is None or not value:
            row.pop(key)
    dynamoTable.put_item(Item=row)
    print("item",count)
    count=count+1
    if count%230==0:
        time.sleep(60)







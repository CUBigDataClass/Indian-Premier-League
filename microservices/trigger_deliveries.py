import json
import boto3
from botocore.vendored import requests


def lambda_handler(event, context):
    # TODO implement
    currentEvent = event['Records'][0]['dynamodb']['NewImage']

    for key, valueDict in currentEvent.items():
        for dataType, finalValue in valueDict.items():
            if dataType == 'N':
                currentEvent[key] = float(finalValue)
            elif dataType == 'S':
                currentEvent[key] = str(finalValue)

    print(currentEvent)
    response = requests.post('http://3.81.127.46:1956/', json=json.dumps(currentEvent))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

import json
import boto3
from botocore.vendored import requests

s3 = boto3.client('s3')
response = s3.get_object(Bucket='bda-configurations', Key='es-config.json')
es_config = (json.loads(response['Body'].read()))


def insert_into_es(each_doc, _id):
    insert_request = requests.post(
        url="{}/{}/_doc/{}".format(es_config['es_url'], es_config['es_deliveries_index'], _id),
        data=json.dumps(each_doc),
        headers=es_config['es_request_headers']).json()
    print(insert_request)


def lambda_handler(event, context):
    # TODO implement

    for each_ in event['Records']:
        action = each_['eventName']

        if (action == 'INSERT' or action == 'MODIFY'):

            currentEvent = each_['dynamodb']['NewImage']
            for key, valueDict in currentEvent.items():
                for dataType, finalValue in valueDict.items():
                    if dataType == 'N':
                        currentEvent[key] = float(finalValue)
                    elif dataType == 'S':
                        currentEvent[key] = str(finalValue)

            insert_into_es(currentEvent, currentEvent['uid'])

    # response = requests.post('http://34.227.172.158:3718/', json=json.dumps(currentEvent))

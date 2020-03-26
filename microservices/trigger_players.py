import json
import boto3
from botocore.vendored import requests

s3 = boto3.client('s3')
response = s3.get_object(Bucket='bda-configurations', Key='es-config.json')
es_config = (json.loads(response['Body'].read()))


def insert_into_es(each_doc, _id):
    insert_request = requests.post(url="{}/{}/_doc/{}".format(es_config['es_url'], es_config['es_players_index'], _id),
                                       data=json.dumps(each_doc),
                                       headers=es_config['es_request_headers']).json()
    print(insert_request)


def lambda_handler(event, context):
    # TODO implement
    action = event['Records'][0]['eventName']
    
    if (action == 'INSERT' or action == 'MODIFY'):

        currentEvent = event['Records'][0]['dynamodb']['NewImage']
        for key, valueDict in currentEvent.items():
            for dataType, finalValue in valueDict.items():
                if dataType == 'N':
                    currentEvent[key] = float(finalValue)
                elif dataType == 'S':
                    currentEvent[key] = str(finalValue)
    
        print(currentEvent)
        insert_into_es(currentEvent, currentEvent['uid'])
        
    
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
    # response = requests.post('http://34.227.172.158:3718/', json=json.dumps(currentEvent))

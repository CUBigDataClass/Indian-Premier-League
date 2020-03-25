import json
import boto3
from botocore.vendored import requests

s3 = boto3.client('s3')
response = s3.get_object(Bucket='radicalist-es-configuration', Key='es_config.json')
es_config = (json.loads(response['Body'].read()))


def es_search_results(search_request):
    es_search_results = requests.post(
        url="{}/{}/_search".format(es_config['es_url'], es_config['es_application_form_index']),
        auth=bauth,
        data=search_request,
        headers=es_config['es_request_headers']).json()
    return es_search_results


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
    response = requests.post('http://34.227.172.158:3718/', json=json.dumps(currentEvent))

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

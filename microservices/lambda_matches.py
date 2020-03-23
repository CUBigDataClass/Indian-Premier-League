import json

def lambda_handler(event, context):
    import json
    import requests
    from elasticsearch import Elasticsearch
    es = Elasticsearch(['localhost'],port=1956)
    newRecord=event['Records'][0]['dynamodb']['NewImage']
    new_dict=dict()
    for key in newRecord.keys():
        recordValue=newRecord[key]
        for key1 in recordValue.keys():
            if key1=="N":
                new_dict[key]=int(recordValue[key1])
            else:
                new_dict[key]=recordValue[key1]
    eventJson=json.dumps(new_dict)
    print(eventJson)
    
    
    # TODO implement
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }

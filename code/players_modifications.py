import requests
import json




# es_config = (json.loads(response['Body'].read()))
with open('../configurations/es-config.json') as f:
  es_config = json.load(f)
# print(es_config)
with open('../data/delivery_with_uid.json') as f:
  player_id_map = json.load(f)
# player_id_map = (json.loads(response_2['Body'].read()))


def insert_into_es(each_doc, index, _id):
    try:
        insert_request = requests.post(url="{}/{}/_doc/{}".format(es_config['es_url'], index, _id),
                                       data=json.dumps(each_doc),
                                       headers=es_config['es_request_headers']).json()
        # print(each_doc,index,insert_request)
        # print(each_doc, index, _id)

    except Exception as es:
        print(each_doc, index, _id,"exception",insert_request)
        print(str(es))
        exit(0)



response = requests.get("http://bdaipl.tech:3718/players/_search?size=600").json()
for each_hit in response['hits']['hits']:
    new_ = each_hit['_source']

    new_['average'] = 0
    if 'balls_bowled' in new_ and 'total_wickets' in new_ and new_['total_wickets'] > 0:
        new_['average'] = (new_['balls_bowled']/new_['total_wickets'])
    # new_['economy'] = 0
    # if 'balls_bowled' in new_ and 'total_runs_given' in new_ and new_['balls_bowled'] > 0:
    #     new_['economy'] = 6 * (new_['total_runs_given'] / new_['balls_bowled'])

    print(new_['average'])

    insert_into_es(new_, 'players', new_['uid'])

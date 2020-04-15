import json
import boto3
from botocore.vendored import requests

s3 = boto3.client('s3')
response = s3.get_object(Bucket='bda-configurations', Key='es-config.json')
es_config = (json.loads(response['Body'].read()))


def insert_into_es(each_doc, index, _id):
    insert_request = requests.post(url="{}/{}/_doc/{}".format(es_config['es_url'], index, _id),
                                   data=json.dumps(each_doc),
                                   headers=es_config['es_request_headers']).json()
    print(insert_request)


def get_response(_id):
    match_info_response = requests.get(
        "{}/{}/_doc/{}".format(es_config['es_url'], es_config['es_deliveries_index'], _id)).json()

    return match_info_response


def update(pub_json, match_info_response):
    if match_info_response['found']:
        match_info = match_info_response['_source']

        # Initialize batsman and bowler dictionaries to setup a player's combined profile
        if pub_json['batsman'] not in match_info:
            match_info[pub_json['batsman']] = {}
        if pub_json['bowler'] not in match_info:
            match_info[pub_json['bowler']] = {}

        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize total runs (innings 1 and 2 separately), in parallel with balls faced if the player is a batsman
        if 'total_runs_inn1' not in match_info:
            match_info['total_runs_inn1'] = 0
        if 'total_runs_inn2' not in match_info:
            match_info['total_runs_inn2'] = 0
        if 'total_runs' not in match_info:
            match_info['total_runs'] = 0
        if 'total_runs' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_runs'] = 0
        if 'balls_faced' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['balls_faced'] = 0

        #   Update total runs (innings 1 and 2 separately), in parallel with balls faced if the player is a batsman
        if pub_json['inning'] == 1:
            match_info['total_runs_inn1'] += pub_json['total_runs']
        if pub_json['inning'] == 2:
            match_info['total_runs_inn2'] += pub_json['total_runs']
        match_info['total_runs'] += pub_json['total_runs']
        match_info[pub_json['batsman']]['total_runs'] += pub_json['total_runs']
        match_info[pub_json['batsman']]['balls_faced'] += 1
        #   -------------------------------------------------------------------------------------------------------    #

        #   -------------------------------------------------------------------------------------------------------    #
        #   Initilalize total 0s, 1s, 2s, 3s, 4s, 5s and 6s for the entire match to zero
        if 'total_0s' not in match_info:
            match_info['total_0s'] = 0
        if 'total_1s' not in match_info:
            match_info['total_1s'] = 0
        if 'total_2s' not in match_info:
            match_info['total_2s'] = 0
        if 'total_3s' not in match_info:
            match_info['total_3s'] = 0
        if 'total_4s' not in match_info:
            match_info['total_4s'] = 0
        if 'total_5s' not in match_info:
            match_info['total_5s'] = 0
        if 'total_6s' not in match_info:
            match_info['total_6s'] = 0

        #   Initialize total 0s, 1s, 2s, 3s, 4s, 5s and 6s of the batsman for the entire match to zero
        if 'total_0s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_0s'] = 0
        if 'total_1s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_1s'] = 0
        if 'total_2s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_2s'] = 0
        if 'total_3s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_3s'] = 0
        if 'total_4s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_4s'] = 0
        if 'total_5s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_5s'] = 0
        if 'total_6s' not in match_info[pub_json['batsman']]:
            match_info[pub_json['batsman']]['total_6s'] = 0

        #   Update total 0s, 1s, 2s, 3s, 4s, 5s and 6s of the match along with the corresponding batsman accordingly
        if pub_json['total_runs'] == 0:
            match_info['total_0s'] += 1
            match_info[pub_json['batsman']]['total_0s'] += 1
        if pub_json['total_runs'] == 1:
            match_info['total_1s'] += 1
            match_info[pub_json['batsman']]['total_1s'] += 1
        if pub_json['total_runs'] == 2:
            match_info['total_2s'] += 1
            match_info[pub_json['batsman']]['total_2s'] += 1
        if pub_json['total_runs'] == 3:
            match_info['total_3s'] += 1
            match_info[pub_json['batsman']]['total_3s'] += 1
        if pub_json['total_runs'] == 4:
            match_info['total_4s'] += 1
            match_info[pub_json['batsman']]['total_4s'] += 1
        if pub_json['total_runs'] == 5:
            match_info['total_5s'] += 1
            match_info[pub_json['batsman']]['total_5s'] += 1
        if pub_json['total_runs'] >= 6:
            match_info['total_6s'] += 1
            match_info[pub_json['batsman']]['total_6s'] += 1
        #   -------------------------------------------------------------------------------------------------------    #

        #   -------------------------------------------------------------------------------------------------------    #
        #   Initilalize total 0s, 1s, 2s, 3s, 4s, 5s and 6s for the first innings to zero
        if 'total_0s_inn1' not in match_info:
            match_info['total_0s_inn1'] = 0
        if 'total_1s_inn1' not in match_info:
            match_info['total_1s_inn1'] = 0
        if 'total_2s_inn1' not in match_info:
            match_info['total_2s_inn1'] = 0
        if 'total_3s_inn1' not in match_info:
            match_info['total_3s_inn1'] = 0
        if 'total_4s_inn1' not in match_info:
            match_info['total_4s_inn1'] = 0
        if 'total_5s_inn1' not in match_info:
            match_info['total_5s_inn1'] = 0
        if 'total_6s_inn1' not in match_info:
            match_info['total_6s_inn1'] = 0

        #   Update total 0s, 1s, 2s, 3s, 4s, 5s and 6s for the first innings accordingly
        if pub_json['total_runs'] == 0 and pub_json['inning'] == 1:
            match_info['total_0s_inn1'] += 1
        if pub_json['total_runs'] == 1 and pub_json['inning'] == 1:
            match_info['total_1s_inn1'] += 1
        if pub_json['total_runs'] == 2 and pub_json['inning'] == 1:
            match_info['total_2s_inn1'] += 1
        if pub_json['total_runs'] == 3 and pub_json['inning'] == 1:
            match_info['total_3s_inn1'] += 1
        if pub_json['total_runs'] == 4 and pub_json['inning'] == 1:
            match_info['total_4s_inn1'] += 1
        if pub_json['total_runs'] == 5 and pub_json['inning'] == 1:
            match_info['total_5s_inn1'] += 1
        if pub_json['total_runs'] >= 6 and pub_json['inning'] == 1:
            match_info['total_6s_inn1'] += 1
        #   -------------------------------------------------------------------------------------------------------    #

        #   -------------------------------------------------------------------------------------------------------    #
        #   Initilalize total 0s, 1s, 2s, 3s, 4s, 5s and 6s for the second innings to zero
        if 'total_0s_inn2' not in match_info:
            match_info['total_0s_inn2'] = 0
        if 'total_1s_inn2' not in match_info:
            match_info['total_1s_inn2'] = 0
        if 'total_2s_inn2' not in match_info:
            match_info['total_2s_inn2'] = 0
        if 'total_3s_inn2' not in match_info:
            match_info['total_3s_inn2'] = 0
        if 'total_4s_inn2' not in match_info:
            match_info['total_4s_inn2'] = 0
        if 'total_5s_inn2' not in match_info:
            match_info['total_5s_inn2'] = 0
        if 'total_6s_inn2' not in match_info:
            match_info['total_6s_inn2'] = 0

        #   Update total 0s, 1s, 2s, 3s, 4s, 5s and 6s for the second innings accordingly
        if pub_json['total_runs'] == 0 and pub_json['inning'] == 2:
            match_info['total_0s_inn2'] += 1
        if pub_json['total_runs'] == 1 and pub_json['inning'] == 2:
            match_info['total_1s_inn2'] += 1
        if pub_json['total_runs'] == 2 and pub_json['inning'] == 2:
            match_info['total_2s_inn2'] += 1
        if pub_json['total_runs'] == 3 and pub_json['inning'] == 2:
            match_info['total_3s_inn2'] += 1
        if pub_json['total_runs'] == 4 and pub_json['inning'] == 2:
            match_info['total_4s_inn2'] += 1
        if pub_json['total_runs'] == 5 and pub_json['inning'] == 2:
            match_info['total_5s_inn2'] += 1
        if pub_json['total_runs'] >= 6 and pub_json['inning'] == 2:
            match_info['total_6s_inn2'] += 1
        #   -------------------------------------------------------------------------------------------------------    #

        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize total extras and total wickets for the entire match
        if 'total_extras' not in match_info:
            match_info['total_extras'] = 0
        if 'total_wickets' not in match_info:
            match_info['total_wickets'] = 0

        #   Update total extras and total wickets for the entire match
        if pub_json['extra_runs'] != 0:
            match_info['total_extras'] += pub_json['extra_runs']
        if pub_json['dismissal_kind'] != 'Not Dismissed':
            match_info['total_wickets'] += 1
        #   -------------------------------------------------------------------------------------------------------    #

        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize total extras and total wickets for the first innings
        if 'total_extras_inn1' not in match_info:
            match_info['total_extras_inn1'] = 0
        if 'total_wickets_inn1' not in match_info:
            match_info['total_wickets_inn1'] = 0

        #   Update total extras and total wickets for the first innings
        if pub_json['extra_runs'] != 0 and pub_json['inning'] == 1:
            match_info['total_extras_inn1'] += pub_json['extra_runs']
        if pub_json['dismissal_kind'] != 'Not Dismissed' and pub_json['inning'] == 1:
            match_info['total_wickets_inn1'] += 1
        #   -------------------------------------------------------------------------------------------------------    #

        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize total extras and total wickets for the second innings
        if 'total_extras_inn2' not in match_info:
            match_info['total_extras_inn2'] = 0
        if 'total_wickets_inn2' not in match_info:
            match_info['total_wickets_inn2'] = 0

        #   Update total extras and total wickets for the second innings
        if pub_json['extra_runs'] != 0 and pub_json['inning'] == 2:
            match_info['total_extras_inn2'] += pub_json['extra_runs']
        if pub_json['dismissal_kind'] != 'Not Dismissed' and pub_json['inning'] == 2:
            match_info['total_wickets_inn2'] += 1
        #   -------------------------------------------------------------------------------------------------------    #

        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize and update balls bowled of a particular player if balls bowled
        if 'balls_bowled' not in match_info[pub_json['bowler']]:
            match_info[pub_json['bowler']]['balls_bowled'] = 0

        match_info[pub_json['bowler']]['balls_bowled'] += 1
        #   -------------------------------------------------------------------------------------------------------    #

        #   -------------------------------------------------------------------------------------------------------    #
        #   Initialize or update number of wickets for a player if wicket taken
        if pub_json['dismissal_kind'] != 'Not Dismissed':
            if 'wickets' in match_info[pub_json['bowler']]:
                match_info[pub_json['bowler']]['wickets'] += 1
            else:
                match_info[pub_json['bowler']]['wickets'] = 1
        #   -------------------------------------------------------------------------------------------------------    #

    return match_info


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

            match_info_response = get_response(currentEvent['uid'])
            match_info = update(currentEvent, match_info_response)
            insert_into_es(currentEvent, es_config['es_deliveries_index'], currentEvent['uid'])
            insert_into_es(match_info, es_config['es_matches_index'], int(match_info['match_id']))

    # response = requests.post('http://34.227.172.158:3718/', json=json.dumps(currentEvent))

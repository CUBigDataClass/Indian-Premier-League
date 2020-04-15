import json
import boto3
import uuid

client = boto3.resource('dynamodb',
                        aws_access_key_id='AKIAWGMK4MS7D3HOP7SJ',
                        aws_secret_access_key='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',
                        region_name='ap-south-1')
table = client.Table('players')
players_set = set()
pending_players_set = set ()
players_uid = set()




def insert_dynamodb(json_data):
    # print(json_data)
    table.put_item(Item=(json_data))

with open('../data/delivery_with_uid.json') as f:
  players_data = json.load(f)
  for each_ in players_data:
      players_set.add(each_)
      if players_data[each_] in players_uid:
          print(players_data[each_],each_)
      else:
          players_uid.add(players_data[each_])

print(len(players_uid), len(players_set))
exit(0)


with open('../data/deliveries/deliveries.json') as f:
  data = json.load(f)
  for each_ in data:
      if data[each_]['batsman'] not in players_set:
          pending_players_set.add(data[each_]['batsman'])
          # print(data[each_]['batsman'])
      if data[each_]['non_striker'] not in players_set:
          pending_players_set.add(data[each_]['non_striker'])
          # print(data[each_]['non_striker'])
      if data[each_]['bowler'] not in players_set:
          pending_players_set.add(data[each_]['bowler'])
          # print(data[each_]['bowler'])


print(pending_players_set)

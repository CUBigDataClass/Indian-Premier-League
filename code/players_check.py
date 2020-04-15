import json
players_set = set()
pending_players_set = set ()


with open('../data/delivery_with_uid.json') as f:
  players_data = json.load(f)
  for each_ in players_data:
      players_set.add(each_)


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

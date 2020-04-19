import json
missing_set = set()
with open('../data/delivery_with_uid.json') as f:
  player_id_map = json.load(f)




with open('../data/deliveries/deliveries.json') as f:
  deliveries = json.load(f)
for each_ in deliveries:
    # print(deliveries[each_]['batsman'],deliveries[each_]['non_striker'],deliveries[each_]['bowler'])
    if deliveries[each_]['batsman'] not in player_id_map:
        missing_set.add(deliveries[each_]['batsman'])
    if deliveries[each_]['non_striker'] not in player_id_map:
        missing_set.add(deliveries[each_]['non_striker'])
    if deliveries[each_]['bowler'] not in player_id_map:
        missing_set.add(deliveries[each_]['bowler'])
print(missing_set)



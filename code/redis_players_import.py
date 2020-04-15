import redis
import json

r = redis.Redis(host='52.54.250.17', port=6379, db=0)
with open('../data/deliveries/deliveryPlayer_with_uid.json') as f:
  data = json.load(f)
  # print(data)
  for each_ in data:
      print(each_)
      r.set(each_, data[each_])
      # exit(0)
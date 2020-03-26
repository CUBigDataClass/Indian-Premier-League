import wikipedia
from bs4 import BeautifulSoup
import requests
import reverse_geocode
import pandas as pd
import geopy.geocoders
from geopy.geocoders import Nominatim
import ssl
import certifi
import os
import json


# not_found = []
# directory = '../Indian-Premier-League/data/players'
#
# count_yes = 0
# count_no = 0
# dt = {}
# for filename in os.listdir(directory):
#     if filename.endswith(".json"):
#         player_name = filename.split('.')[0]
#     try:
#         count_yes+=1
#         py = wikipedia.page(player_name)
#     except:
#         pass
#         # count_no+=1
#         # not_found.append(player_name)
#
#     link = py.url
#
#     page = requests.get(link).text
#
#     html = BeautifulSoup(page, 'html.parser')
#
#     ctx = ssl.create_default_context(cafile=certifi.where())
#     geopy.geocoders.options.default_ssl_context = ctx
#
#     geolocator = Nominatim()
#
#     birthplace = html.find_all('span', {'class':"birthplace"})
#     for link in birthplace:
#         name = link.find('a')
#         try:
#             place = name.get_text('title')
#             location = geolocator.geocode(place)
#             # print(location.latitude, location.longitude)
#             dt[player_name] = {"birthplace":place,
#                                 "latitude":location.latitude,
#                                 "longitude":location.longitude}
#         except:
#             print(player_name)
#             dt[player_name] = {"birthplace": None,
#                                 "latitude": 0.0,
#                                 "longitude": 0.0}
#
#
# print(count_yes)
# print(count_no)
# for i in dt.items():
#     print(i)
#
# print("before",len(dt))
#
# dt['Trent Boult'] = {'birthplace':'Rotorua',
#                      'latitude': 38.1368,
#                      'longitude': 176.2497}
#
# dt['Shahbaz Ahamad'] = {'birthplace':'Mewat',
#                         'latitude': 28.010693,
#                         'longitude': 77.056442}
#
# dt['AB de Villiers'] = {'birthplace':'South Africa',
#                         'latitude': 25.7479,
#                         'longitude': 28.2293}
#
# dt['Lalith Yadav'] = {'birthplace': None,
#                         'latitude': 0.0,
#                         'longitude': 0.0}
#
# dt['MS Dhoni'] = {'birthplace': 'Ranchi',
#                         'latitude': 23.3441,
#                         'longitude': 85.3096}
#
# dt['Sanjay Yadav'] = {'birthplace': 'Gorakhpur',
#                         'latitude': 26.7588,
#                         'longitude': 83.3697}
#
# dt['Ben Stokes'] = {'birthplace': 'Christchurch',
#                         'latitude': -43.53,
#                         'longitude': 172.620278}
#
# dt['Mohammad Shami'] = {'birthplace': 'Amroha',
#                         'latitude': 28.904431,
#                         'longitude': 78.467528}
#
# dt['Anirudha Joshi'] = {'birthplace': 'Bangalore',
#                         'latitude': 12.983333,
#                         'longitude': 77.583333}
#
# dt['Akash Singh'] = {'birthplace': None,
#                         'latitude': 0.0,
#                         'longitude': 0.0}
#
# print("After", len(dt))
# data = pd.DataFrame.from_dict(dt, orient='index')
# data.to_csv("../Indian-Premier-League/data/players/data.csv")

data = pd.read_csv("../Indian-Premier-League/data/players/data.csv")
list_tuples = list(zip(data.latitude, data.longitude))

# print(list_tuples)

rows = []
for e in reverse_geocode.search(list_tuples):
    rows.append(pd.DataFrame.from_dict(e, orient='index').T)

subset = pd.concat(rows)
subset.reset_index(drop=True, inplace=True)

final_data = pd.concat([data, subset], axis=1, ignore_index=True)

final_data.rename(columns={"Unnamed: 0": "player_name"}, inplace=True)
# print(final_data)
# final_data.to_csv("../Indian-Premier-League/data/players/final_data.csv")
with open('../Indian-Premier-League/data/players/player_birth_info.json', 'w') as json_file:
    json.dump(final_data.to_dict('records'), json_file, indent=8)

 pushing into dynamo db


# json_data = final_data.to_json(orient='records')

# print(json_data)



table = dynamo_db.Table('players')

with open('../Indian-Premier-League/data/player_birth_info.json') as json_file:
    json_data = json.load(json_file,parse_float = decimal.Decimal)


print(json_data)

count = 0
for key in json_data:
    print(count)
    # if (count % 100 == 0):
        # print(count, 'items done')
    table.put_item(Item=json_data[key])
    count += 1

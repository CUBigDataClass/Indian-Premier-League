import selenium
import pandas as pd
import bs4
from bs4 import BeautifulSoup
import requests
import json
import re

# Specify URL address of the any player
URL = 'https://www.iplt20.com/teams/chennai-super-kings/squad/1/ms-dhoni'

for URL in URLs:
    team_name = URL.split('/')[4]
    page = requests.get(URL).text
    player_info = {}

    html = BeautifulSoup(page, 'html.parser')

    try:
        h1_detail = html.find_all('h1', {'class': "player-hero__name player-hero__name--captain"})
    except:
        pass

    try:
        h1_detail = html.find_all('h1', {'class': "player-hero__name"})
    except:
        print("Not Captain")

    player_name = [h.get_text() for h in h1_detail]

    name = player_name[0]
    print(name)
    player_info[name] = {}
    player_info[name]["team_name"] = team_name


    spans_labels = html.find_all('span', {'class': 'player-stats__label'})
        

    spans_values = html.find_all('span', {'class': 'player-stats__value'})

    lines_labels = [span.get_text() for span in spans_labels]
        

    lines_values = [span.get_text() for span in spans_values]
        

    player_stats = dict(zip(lines_labels, lines_values))
    player_info[name]["stats"] = player_stats

    tds_label = html.find_all('td', {'class': 'player-details__label'})
        
    tds_value = html.find_all('td', {'class': 'player-details__value'})

    td_labels = [t.get_text() for t in tds_label]
    td_values = [t.get_text() for t in tds_value]


    player_details = dict(zip(td_labels, td_values))
        
    player_info[name]["details"] = player_details

    try:
        tables = pd.read_html(page)
    except:
        pass

    try:
        tables[2]['HS'] = tables[2]['HS'].map(lambda x: re.sub(r'\W+', '', x))
    except:
        print("no special characters")

    print('\n')

    try:
        player_info[name]["Batting and Fielding"] = tables[2].to_dict('records')
    except:
        print("No Batting and Fielding Table")

    print('\n')


    try:
        player_info[name]["Bowling"] = tables[3].to_dict('records')
    except:
        print("No Bowling Table")

    print(player_info)


    with open('/Users/lokin/Documents/IPL_player_data/'+name+'.json', 'w') as json_file:
        json.dump(player_info, json_file, indent=8)

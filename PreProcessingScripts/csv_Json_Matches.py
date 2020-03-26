import csv
import json
import datetime
import re
csvfile='D:\CUB\Spring20\BigDataArchitecture\Project\matches.csv'
jsonfile='D:\CUB\Spring20\BigDataArchitecture\Project\matches.json'

lines1=[]
out1=[]


with open(csvfile) as csvfile1:
    reader_in=csv.DictReader(csvfile1)
    rows=[]
    for row in reader_in:
        #row['id']=int(row['id'])
        row['season']=int(row['season'])
        row['date']=re.sub(r'(\d+)-(\d+)-(\d+)', r'\2/\3/\1', row['date'])
        row['dl_applied']=int(row['dl_applied'])
        row['win_by_runs']=int(row['win_by_runs'])
        row['win_by_wickets']=int(row['win_by_wickets'])
        # print(row['date'])
        rows.append(row)
with open(jsonfile,'w') as jsonfile1:
    jsonfile1.write(json.dumps(rows,indent=4))

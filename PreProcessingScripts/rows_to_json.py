import pandas, json, os

rows = pandas.read_csv('matches.csv')
# rows.drop(columns=['Unnamed: 0'], inplace=True)
folder_path = 'json_files_matches'
# print(rows.columns)

for index, row in rows.iterrows():
    current_dict = {}
    for col in rows.columns:
        file_name = str(row['id']) + '.json'
        file_path = os.path.join(folder_path, file_name)
        current_dict[col] = row[col]
        # if col != 'id':
        #     current_dict[col] = row[col]
        with open(file_path, 'w') as fp:
            json.dump(current_dict, fp)
    print(row['id'], index)

import csv
import json

slug_list = []

with open('data/pokemon.csv', mode='r', encoding='utf-8') as file:
    csvFile = csv.DictReader(file)

    for row in csvFile:
        id_value = int(row['id'])
        if 1 <= id_value <= 1010:
            slug_list.append(row['slug'])

with open('data/pokemon_names.json', 'w') as json_file:
    for index, slug in enumerate(slug_list):
        json.dump(slug, json_file)
        if index != len(slug_list) - 1:
            json_file.write('\n')

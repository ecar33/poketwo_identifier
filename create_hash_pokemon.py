import json
from itertools import product
import pickle

pokemon_name_and_length = []
all_hint_combinations = {}

with open('data/pokemon_names.json', 'r') as json_file:

    for line in json_file:
        parsed_json = json.loads(line.strip())

        pokemon_name_and_length.append((parsed_json, len(parsed_json)))

for name, size in pokemon_name_and_length:
    for combination in product([0,1], repeat = size):
        combination_str = ''.join(map(str, combination))

        if combination_str not in all_hint_combinations:
            all_hint_combinations[combination_str] = [name]

        else:
            all_hint_combinations[combination_str].append(name)


# Serialize (save)
with open('data/all_hint_combinations.pkl', 'wb') as f:
    pickle.dump(all_hint_combinations, f)






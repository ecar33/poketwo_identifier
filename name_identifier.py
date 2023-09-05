import pickle
import re

def convert_to_binary(hint):
    binary_hint = ''
    for char in hint.lower():
        if char != '_':
            binary_hint += '1'
        else:
            binary_hint += '0'

    return binary_hint

def search_dict_for_pokemon(binary_hint, hint, all_hint_combinations):
    list_of_possible_matches = all_hint_combinations[binary_hint]

    for pokemon in list_of_possible_matches:
        pokemon_char_index = 0
        match = True
        for char in hint:
            if char != '_':
                if char.lower() != pokemon[pokemon_char_index].lower():
                    match = False
                    break
            pokemon_char_index += 1

        if match:
            return pokemon

def capture_pokemon_hint(hint_string):
    match = re.search("The pokémon is (.+?)\.", hint_string)
    hint = match.group(1)
    return hint


def main(hint):
    with open('data/all_hint_combinations.pkl', 'rb') as f:
        # Unload pickle
        loaded_all_hint_combinations = pickle.load(f)

    # For testing as a script directly
    # hint_string = "The pokémon is F___zen."
    # hint = capture_pokemon_hint(hint_string)

    binary_hint = convert_to_binary(hint)

    solution = search_dict_for_pokemon(binary_hint, hint, loaded_all_hint_combinations)

    return solution

if __name__ == "__main__":
    main()

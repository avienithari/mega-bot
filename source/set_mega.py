from collections import Counter
import requests


def get_typings(spawn_list):
    type_list = []
    try:
        for spawn in spawn_list: 
            pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{spawn}").json()
            if len(pokemon["types"]) == 1:
                type_list.append((pokemon["types"][0]["type"]["name"],))
            else:
                type_list.append((pokemon["types"][0]["type"]["name"], pokemon["types"][1]["type"]["name"]))

        return type_list
    except Exception as e:
        print(e)
        return "Error occured"

def pick_mega(mega_types, type_list):
    mega = []
    counter = 0
    for pokemon_type in type_list:
        for mega_pokemon_type in mega_types.keys():
            counter += 1
            try:
                if (pokemon_type[0] == mega_types[mega_pokemon_type][0] or
                    pokemon_type[0] == mega_types[mega_pokemon_type][1]):
                        mega.append(mega_pokemon_type)
                elif (pokemon_type[1] == mega_types[mega_pokemon_type][0] or
                    pokemon_type[1] == mega_types[mega_pokemon_type][1]):
                        mega.append(mega_pokemon_type)
                elif (pokemon_type[0] == mega_types[mega_pokemon_type][2] or
                    pokemon_type[1] == mega_types[mega_pokemon_type][2]):
                        mega.append(mega_pokemon_type)
            except IndexError:
                continue

    return Counter(mega).most_common(3)

def message(sorted_mega):
    return f"Best mega coverage is provided by:\n{sorted_mega[0][0].title()}\n{sorted_mega[1][0].title()}\n{sorted_mega[2][0].title()}\n"

def set_mega(mega_types, *args):
    event_spawns = list(args)
    type_list = get_typings(event_spawns)
    sorted_mega = pick_mega(mega_types, type_list)
    return message(sorted_mega)

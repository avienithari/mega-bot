import requests


def get_mega_list():
    mega = [
        "venusaur-mega",
        "charizard-mega-x",
        "charizard-mega-y",
        "blastoise-mega",
        "alakazam-mega",
        "gengar-mega",
        "kangaskhan-mega",
        "gyarados-mega",
        "pinsir-mega",
        "aerodactyl-mega",
        "mewtwo-mega-x",
        "mewtwo-mega-y",
        "ampharos-mega",
        "scizor-mega",
        "heracross-mega",
        "houndoom-mega",
        "tyranitar-mega",
        "blaziken-mega",
        "gardevoir-mega",
        "mawile-mega",
        "aggron-mega",
        "medicham-mega",
        "manectric-mega",
        "banette-mega",
        "absol-mega",
        "latias-mega",
        "latios-mega",
        "garchomp-mega",
        "lucario-mega",
        "abomasnow-mega",
        "beedrill-mega",
        "pidgeot-mega",
        "slowbro-mega",
        "steelix-mega",
        "sceptile-mega",
        "swampert-mega",
        "sableye-mega",
        "sharpedo-mega",
        "camerupt-mega",
        "altaria-mega",
        "glalie-mega",
        "salamence-mega",
        "metagross-mega",
        "lopunny-mega",
        "gallade-mega",
        "audino-mega",
        "diancie-mega",
    ]
    primal_types = {
        "primal groudon": ("grass", "fire", "ground"),
        "primal kyogre": ("water", "bug", "electric"),
        "mega rayquaza": ("flying", "dragon", "psychic")
    }

    mega_types = {}
    for m in mega:
        pokemon = requests.get(f"https://pokeapi.co/api/v2/pokemon/{m}").json()
        mega_name = pokemon["name"].split("-")
        if len(mega_name) == 2:
            mega_name = " ".join(pokemon["name"].split("-")[::-1])
        else:
            mega_name = pokemon["name"].split("-")[::-1]
            temp = mega_name.pop(0)
            mega_name.append(temp)
            mega_name = " ".join(mega_name)

        if len(pokemon["types"]) == 1:
            mega_types[mega_name] = (pokemon["types"][0]["type"]["name"],)
        else:
            mega_types[mega_name] = (pokemon["types"][0]["type"]["name"], pokemon["types"][1]["type"]["name"])

    mega_types.update(primal_types)
    return mega_types

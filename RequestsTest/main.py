import requests

URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = 'fcc978602acd7a44fe1b749c3880487c'

HEADER = {'Content-Type': 'application/json', 'trainer_token': 'fcc978602acd7a44fe1b749c3880487c'}

body_post_pokemons = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_put_pokemons = {
    "pokemon_id": "231769",
    "name": "Петр",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "231769"
}

generate_pokemon=requests.post(url = f'{URL}/pokemons', json = body_post_pokemons, headers=HEADER)
print(generate_pokemon.text)

update_name_pokemon=requests.put(url = f'{URL}/pokemons', json = body_put_pokemons, headers=HEADER)
print(update_name_pokemon.text)

add_pokeball_pokemon=requests.post(url = f'{URL}/trainers/add_pokeball', json = body_add_pokeball, headers=HEADER)
print(add_pokeball_pokemon.text)
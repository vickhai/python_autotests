import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'

TOKEN = 'fcc978602acd7a44fe1b749c3880487c'

HEADER = {'Content-Type': 'application/json', 'trainer_token': 'fcc978602acd7a44fe1b749c3880487c'}

TRAINER_ID = '20101'

def test_status_code():
    response = requests.get(url = f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_part_of_response():
    response_get = requests.get(url = f'{URL}/pokemons', params={'trainer_id':TRAINER_ID})
    print(response_get.json())
    assert response_get.json()['data'][0]['name'] == 'Бульбазавр'
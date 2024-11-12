import requests
import pytest


URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' :'application/json', 'trainer_token' : '0a9afaee933fcd3bf2f544c3e3068a86'}
TRAINER_ID = '7751'

def test_status_code():
    response = requests.get(url= f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response.status_code == 200

def test_part_trainer():
    response_get = requests.get(url= f'{URL}/trainers', params= {'trainer_id': TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'IvAna'
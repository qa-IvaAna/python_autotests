import requests

URL = 'https://api.pokemonbattle.ru/v2'
HEADER = {'Content-Type' :'application/json', 'trainer_token' : '0a9afaee933fcd3bf2f544c3e3068a86'}
body_create = {
    "name": "Бульбазавр",
    "photo_id": 1
}

body_put = {
    "pokemon_id": "130404",
    "name": "King",
    "photo_id": 2
}

body_add_pokeball = {
    "pokemon_id": "130404"
}


response = requests.post(url= f'{URL}/pokemons', headers= HEADER, json = body_create)
print(response.text)

response = requests.put(url= f'{URL}/pokemons', headers=HEADER, json = body_put)
print(response.text)

response = requests.post(url= f'{URL}/trainers/add_pokeball', headers= HEADER, json =  body_add_pokeball)
print(response.text)
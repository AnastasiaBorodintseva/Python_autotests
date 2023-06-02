import requests

token = '3e1901333ef00752fd23fdfab11b599d'

body_create = {
    "name":"Butterfree",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

header = {"Content-Type" : "application/json", "trainer_token" : token}

pokemon_id = requests.post('https://pokemonbattle.me:9104/pokemons', json=body_create, headers = header).json().get("id")

print("ID покемона: ", pokemon_id)

body_update = {
    "pokemon_id": str(pokemon_id),
    "name": "Mememememe",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}

answer_update = requests.put('https://pokemonbattle.me:9104/pokemons', json=body_update, headers = header)

print(answer_update.text)

body_pokeball = {
    "pokemon_id": str(pokemon_id)
}

answer_pokeball = requests.post('https://pokemonbattle.me:9104/trainers/add_pokeball', json=body_pokeball, headers = header)

print(answer_pokeball.text)

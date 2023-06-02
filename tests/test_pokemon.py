import requests
import pytest

host = 'https://pokemonbattle.me:9104'
token = '3e1901333ef00752fd23fdfab11b599d'

def test_status_code():
    answer = requests.get(f'{host}/trainers', headers= {'trainer_token': token})
    assert answer.status_code == 200

def test_part_of_answer():
    answer_body = requests.get(f'{host}/trainers', params = {'trainer_id' : 4631})
    assert answer_body.json()['trainer_name'] == 'Marie'

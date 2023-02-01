import requests
import random
import json


def test_create_valid_board():
    token_value = "ATTA6da12a38b514097498c043608314e514a5deb8e52523e233dbff9fd7ef7a2100CCE2DFF3"
    key_value = "bae166012ae2cf255c73d6d777c61db0"
    random_name = "board_0"
    url = "https://api.trello.com/1/boards/"

    query_params = {
        "key": key_value,
        "token": token_value,
        "name": random_name
    }
    se = requests.Session()
    response = se.post(
        url, params=query_params
    )
    assert response.status_code == 200


def test_prefs_card_covers_false():
    token_value = "ATTA6da12a38b514097498c043608314e514a5deb8e52523e233dbff9fd7ef7a2100CCE2DFF3"
    key_value = "bae166012ae2cf255c73d6d777c61db0"
    random_name = "deflist1"
    url = "https://api.trello.com/1/boards/"

    query_params = {
        "key": key_value,
        "token": token_value,
        "name": random_name,
        "prefs": {"prefs_cardCovers": False}

    }

    response = requests.post(
        url, params=query_params
    )
    library = json.loads(response.text) # parse string to dictionary
    board_id = library['id']
    board_name = library['name']
    print(response.status_code)
    assert response.status_code == 200
    get_url = url + board_id
    query_params = {
        "key": key_value,
        "token": token_value
    }
    headers = {
        "Accept": "application/json"}
    response_get = requests.get(
        get_url,
        headers=headers,
        params=query_params
    )
    assert response_get.status_code == 200

    return_get = json.loads(response_get.text)  # parse string to dictionary
    actual_board_name = return_get['name']
    assert random_name == actual_board_name
    requests.delete(
         get_url,
         params=query_params
    )

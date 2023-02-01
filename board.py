import requests
import random


def test_create_valid_board():
    token_value = "ATTA6da12a38b514097498c043608314e514a5deb8e52523e233dbff9fd7ef7a2100CCE2DFF3"
    key_value = "bae166012ae2cf255c73d6d777c61db0"
    random_name = random(5)
    url = "https://api.trello.com/1/boards/"

    query_params = {
        "key": key_value,
        "token": token_value,
        "name": random_name
    }

    response = requests.post(
        url, params=query_params
    )
    assert response.status_code == 200

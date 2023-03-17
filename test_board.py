import requests
import json

import helper
import variables
import context as c


def test_create_valid_board():
    random_name = "board_0"
    query_params = {
        "name": random_name
    }
    query_params.update(variables.authorization)
    response = requests.post(
        variables.board_url, params=query_params
    )
    assert response.status_code == 200


def test_prefs_card_covers_false():
    background_color = "red"
    response = helper.create_board({"defaultList": "false", "prefs_background": background_color})
    assert response.status_code == 200
    board_id = json.loads(response.text)["id"]  # parse string to dictionary
    response = helper.create_board({"idBoardSource": board_id})
    assert response.status_code == 200
    assert json.loads(response.text)["background"] == background_color


def test_clone_board():
    helper.delete_default_organization()
    helper.create_board({"prefs_background": "yellow"})
    random_name = "board_to_be_cloned_1"
    query_params = {
        "name": random_name,
        "prefs_background": "blue",
        "idBoardSource": c.get_context("based_board_id")
    }
    query_params.update(variables.authorization)

    response = requests.post(
        variables.board_url, params=query_params
    )
    assert response.status_code == 200
    assert json.loads(response.text)["background"] == "yellow"

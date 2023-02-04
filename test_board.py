import requests
import json

import variables
import variables as v


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
    # random_name = "deflist1"
    # query_params = {
    #     "name": random_name,
    #     "prefs": {"prefs_cardCovers": False}
    # }
    # query_params.update(v.authorization)
    #
    # response = requests.post(
    #     v.board_url, params=query_params
    # )
    # assert response.status_code == 200
    # library = json.loads(response.text)  # parse string to dictionary
    # board_id = library['id']

    board_id = "63de3570d91006c1b0e83cd5"
    response_get = get_board_by_id(board_id, 200)
    # return_get = json.loads(response_get.text)  # parse string to dictionary
    # actual_board_name = return_get['name']
    # assert random_name == actual_board_name
    #
    # delete_board_by_id(board_id, 200)


def get_board_by_id(board_id, status_code):
    url = v.board_url + board_id
    headers = {
        "Accept": "application/json"}
    res = requests.get(
        url,
        headers=headers,
        params=v.authorization
    )
    assert res.status_code == status_code
    return res


def delete_board_by_id(board_id, status_code):
    url = v.board_url + board_id
    res = requests.delete(
        url,
        params=v.authorization
    )
    assert res.status_code == status_code

def test_clone_board():
    random_name = "board_to_be_cloned"

    query_params = {
        "name": random_name,
        "prefs": {
            "backgroundColor": "#4BBF6B",
            "background": "lime",
            "backgroundBottomColor": "#4BBF6B",
            "backgroundTopColor": "#4BBF6B",
        }
    }
    query_params.update(variables.authorization)
    response = requests.post(
        variables.board_url, params=query_params
    )

    assert response.status_code == 200

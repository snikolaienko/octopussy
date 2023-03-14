import random
import string

import requests
import variables as v
import variables


def create_board(params={}):
    query_params = {
        "name": ''.join(random.choices(string.ascii_lowercase, k=5))
    }
    query_params.update(variables.authorization)
    query_params.update(params)

    response = requests.post(
        variables.board_url, params=query_params)
    return response


def delete_board_by_id(board_id, status_code):
    url = v.board_url + board_id
    res = requests.delete(
        url,
        params=v.authorization
    )
    assert res.status_code == status_code


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

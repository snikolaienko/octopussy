import context as c
import json
import random
import string

import requests
import variables as v
import variables


def create_board(params={}):
    if c.get_context("organization_id"):
        create_organization()
        get = c.get_context("organization_id")
    query_params = {
        "name": ''.join(random.choices(string.ascii_lowercase, k=5)),
        "idOrganization": c.get_context("organization_id")
    }
    query_params.update(variables.authorization)
    query_params.update(params)
    response = requests.post(
        variables.board_url, params=query_params)
    assert response.status_code == 200, "Exception text" + str(json.loads(response.text))
    c.update_context("based_board_id", json.loads(response.text)["id"])


def create_organization(params={}):
    default_name = "MainOrg"
    query_params = {
        "displayName": default_name
    }
    query_params.update(variables.authorization)
    query_params.update(params)
    response = requests.post(
        variables.organizations_url, params=v.authorization)
    c.update_context("organization_id", default_name)
    return response


def delete_board_by_id(board_id, status_code):
    url = v.board_url + board_id
    res = requests.delete(
        url,
        params=v.authorization
    )
    assert res.status_code == status_code


def delete_organization_by_name(org_name):
    if org_name:
        url = v.organizations_url + org_name
        res = requests.delete(
            url,
            params=v.authorization
        )
        assert res.status_code == 204 or res.status_code == 404


def delete_default_organization():
    delete_organization_by_name(c.get_context("organization_name"))


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

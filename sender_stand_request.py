import requests
from requests.auth import HTTPBasicAuth
import configuration
import data
#
basic = HTTPBasicAuth(data.username, data.password)
#
def post_token_auth(body=None):
    if body is None:
        body = {}
    return requests.post(configuration.URL + configuration.TOKEN_PATH, headers=data.headers, json=body)
#


def get_category(params=None):
    if params is None:
        params = {}
    return requests.get(configuration.URL + configuration.CATEGORY_PATH,
                        headers=data.headers, auth=basic, params=params)

def post_category(body=None):
    if body is None:
        body = {}
    return requests.post(configuration.URL + configuration.CATEGORY_PATH, headers=data.headers, auth=basic, json=body)
#
#
#
def get_category_id(id_cat=None):
    if id_cat is not None:
        id_cat = str(id_cat) + "/"
        return requests.get(configuration.URL + configuration.CATEGORY_PATH + id_cat, headers=data.headers, auth=basic)
    else:
        return requests.get(configuration.URL + configuration.URL, headers=data.headers_api, auth=basic)


def get_pet(params=None):
    if params is None:
        params = {}
    return requests.get(configuration.URL + configuration.PET_PATH,
                        headers=data.headers, auth=basic, params=params)


def post_pet(body=None):
    if body is None:
        body = {}
    return requests.post(configuration.URL + configuration.PET_PATH,
                         headers=data.headers, auth=basic, json=body)





import pytest
import requests
from requests.auth import HTTPBasicAuth
import configuration
import sender_stand_request
import random
import string



# Функция для рандомного создания name
def generate_random_string(n):
    name = ""

    for i in range(n):
        name = name + random.choice(string.ascii_letters)
    return name



# Позитивная функция для получения auth_token
def positive_assert_auth_token(username, password):
    body = {"username": username, "password": password}
    resp = sender_stand_request.post_token_auth(body)
    assert resp.status_code == 200
    assert "token" in resp.json()
    assert type("token") == str


# Негативная функция для получения auth_token
def negative_assert_auth_token(username=None, password=None):
    body = {}
    if username is not None:
        body["username"] = username
    if password is not None:
        body["password"] = password
    resp = sender_stand_request.post_token_auth(body)
    if type(username) != str or type(password) != str or username == "" \
            or password == "" or username != "admin" or password != "admin":
        assert resp.status_code == 404
    else:
        assert resp.status_code == 200


# Позитивная функция для получения списка категорий
def positive_assert_get_category(limit, offset):
    params = {"limit": limit, "offset": offset}
    resp = sender_stand_request.get_category(params)
    assert resp.status_code == 200
    assert "count" in resp.json()
    assert "next" in resp.json()
    assert "previous" in resp.json()
    assert "results" in resp.json()


# Негативная функция для получения списка категорий
def negative_assert_get_category(limit, offset):
    params = {"limit": limit, "offset": offset}
    resp = sender_stand_request.get_category(params)
    if type(limit) != int or type(offset) != int:
        print('Please correct the following validation errors and try again.'
              ' Value must be an integer ')
        assert resp.status_code == 404
    else:
        assert resp.status_code == 400


# Позитивная функция для создания категории животного
def positive_assert_post_category(name):
    body = {"name": name}
    resp = sender_stand_request.post_category(body)
    assert resp.status_code == 201
    assert "id" in resp.json()
    assert "name" in resp.json()
    assert resp.json()["name"] == name


# Позитивная функции для  получения категории животного по id
def positive_get_category_id(id_cat):
    resp = sender_stand_request.get_category_id(id_cat)
    assert resp.status_code == 200
    assert "id" in resp.json()
    assert "name" in resp.json()
    assert resp.json()["id"] == id_cat


# Негативная функции для  получения категории животного по id
def negative_get_category_id(id=None):
    resp = configuration.CATEGORY_ID_PATH
    if id is None:
        assert resp.status_code == 200
        assert "count" in resp.json()
    elif type(id) is str:
        print('Please correct the following validation errors and try again. '
              'Value must be an integer')
        assert resp.status_code == 400
    elif id not in list_id_category():
        assert resp.status_code == 404


# Позитивная функция для получения списка животных
def positive_assert_get_pet():
    params = {"limit": limit, "offset": offset}
    resp = sender_stand_request.get_pet(params)
    assert resp.status_code == 200
    assert "count" in resp.json()
    assert "next" in resp.json()
    assert "previous" in resp.json()
    assert "results" in resp.json()


# Позитивная функция получения  животного по id
def positive_get_id_pet(id_pet):
    res = requests_func.get_pet_id(id_pet)
    assert res.status_code == 200
    assert "id" in res.json()
    assert "name" in res.json()
    assert "photo_url" in res.json()
    assert "category" in res.json()
    assert "status" in res.json()



# Негативная функция получения  животного по id
def negative_assert_get_pet(limit=None, offset=None):
    params = {}
    if limit is not None:
        params["limit"] = limit
    if offset is not None:
        params["offset"] = offset
    resp = sender_stand_request.get_pet(params)
    assert resp.status_code == 500



# Проверка получения auth_token с корректным введением логина, пароля
def test_positive_post_token_auth_ok_params():
    positive_assert_auth_token("admin", "admin")


# Проверка получения auth_token, не передав параметры логина, пароля
def test_negative_post_token_auth_None_params():
    negative_assert_auth_token(None, None)


# Проверка получения auth_token, не передав параметры логина
def test_negative_post_token_auth_None_login_params():
    negative_assert_auth_token(None, "admin")


# Проверка получения auth_token, не передав параметры пароля
def test_negative_post_token_auth_None_password_params():
    negative_assert_auth_token("admin", None)


# Проверка получения auth_token, передав неправильные параметры логина и пароля
def test_negative_post_token_auth_wrong_params():
    negative_assert_auth_token("login", "password")


# Проверка получения списка категорий
def test_positive_get_category_None_param():
    positive_assert_get_category(None, None)


# Проверка получения списка категорий с параметпами limit и offset
def test_positive_get_category_with_limit_offset():
    positive_assert_get_category(1, 1)

# Проверка получения списка категорий, если передать строку в параметр limit
def test_negative_get_category_limit_str():
    negative_assert_get_category('limit', 1)


# Проверка получения списка категорий, если передать строку в параметр offset
def test_negative_get_category_offset_str():
    negative_assert_get_category(1, 'offset')


# Проверка получения списка категорий, если передать float в параметр limit, offset
def test_negative_get_category_float_limit_offset():
    negative_assert_get_category(0.5, 0.5)


# Проверка создания категории животного(5 символов в названии)
def test_positive_post_category_name_5_symbols():
    name = generate_random_string(5)
    positive_assert_post_category(name)


# Проверка создания категории животного(150 символов в названии)
def test_positive_post_category_name_150_symbols():
    name = generate_random_string(150)
    positive_assert_post_category(name)


# Негативная проверка создания категории животного(151 символов в названии)
def test_positive_post_category_name_151_symbols():
    name = generate_random_string(151)
    positive_assert_post_category(name)


# Позитивная проверка получения категории животного по id
def test_positive_get_category_real_id():
    positive_get_category_id(1)


# Негативная проверка получения категории животного по id (id - строка)
def test_negative_get_category_id_not_int():
    negative_get_category_id('a')


# Позитивная проверка получения списка животных
def test_positive_get_pet():
    positive_assert_get_pet








import pytest
import requests


@pytest.mark.parametrize('breed_name', ["mastiff", "mountain", "finnish"])
def test_api_sub_breed(base_url_dog_api, breed_name):
    url = f'{base_url_dog_api}/breed/{breed_name}/list'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200
    assert res_json['message'] != []
    assert 'status' in res_json


def test_api_random_image(base_url_dog_api):
    url = f'{base_url_dog_api}/breeds/image/random'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    assert res_json['status'] == 'success', "Incorrect status"
    assert 'message' in res_json, "Incorrect message"


@pytest.mark.parametrize('count', [4, 10, 12, 22, 38])
def test_api_random_image_display_multiple(base_url_dog_api, count):
    url = f'{base_url_dog_api}/breeds/image/random/{count}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    assert res_json['status'] == 'success', "Incorrect status"
    assert 'message' in res_json, "Incorrect message"
    assert count == len(res_json['message']), "The number of requested items does not match the issue"


@pytest.mark.parametrize('breed_name', ["australian", "buhund", "bulldog", "bullterrier", "collie"])
def test_api_by_breed(base_url_dog_api, breed_name):
    url = f'{base_url_dog_api}/breed/{breed_name}/images'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    assert res_json['status'] == 'success', "Incorrect status"
    assert 'message' in res_json, "Incorrect message"
    for item in res_json['message']:
        assert breed_name in item, "Breed is not listed"


@pytest.mark.parametrize('breed_name', ["corgy", "dan", "dole", "lasa", "mexicanairless"])
def test_404_api_by_breed(base_url_dog_api, breed_name):
    url = f'{base_url_dog_api}/breed/{breed_name}/images'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 404, "Incorrect code"
    assert res_json['status'] == 'error', "Incorrect status"
    assert 'message' in res_json, "Incorrect message"
    assert res_json['message'] == "Breed not found (master breed does not exist)"
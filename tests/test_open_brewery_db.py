import pytest
import requests


@pytest.mark.parametrize('breweries_id', ["10-56-brewing-company-knox", "10-barrel-brewing-co-bend-1",
                                          "10-barrel-brewing-co-bend-2", "10-barrel-brewing-co-boise-boise",
                                          "101-brewery-quilcene"])
def test_api_get_brewery_by_id(base_url_openbrewerydb_api, breweries_id):
    url = f'{base_url_openbrewerydb_api}/breweries/{breweries_id}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    assert res_json['id'] == breweries_id


@pytest.mark.parametrize('query', ['Dog', 'Epidemic'])
def test_api_autocomplete(base_url_openbrewerydb_api, query):
    url = f'{base_url_openbrewerydb_api}/breweries/autocomplete?query={query}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    for item in range(len(res_json)):
        assert 'id' in res_json[item], "no id"
        assert query in res_json[item]["name"], "query in not in name"


def test_api_404_get_brewery(base_url_openbrewerydb_api):
    breweries_id = 9876543210
    url = f'{base_url_openbrewerydb_api}/breweries/{breweries_id}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 404, "Incorrect code"
    assert res_json['message'] == f"Couldn't find Brewery"


@pytest.mark.parametrize('city', ['San Diego', 'Los Angeles'])
def test_api_breweries_by_city_1(base_url_openbrewerydb_api, city):
    url = f'{base_url_openbrewerydb_api}/breweries/?by_city={city}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    for item in range(len(res_json)):
        assert 'id' in res_json[item], "no id"
        assert city in res_json[item]["city"], "Incorrect city"


@pytest.mark.parametrize('state', ['San Diego', 'Los Angeles'])
@pytest.mark.parametrize('brewery_type', ['micro', 'regional'])
def test_api_breweries_by_city_2(base_url_openbrewerydb_api, state, brewery_type):
    url = f'{base_url_openbrewerydb_api}/breweries/?by_state={state}&by_type={brewery_type}'
    res = requests.get(url=url)
    res_json = res.json()
    assert res.status_code == 200, "Incorrect code"
    for item in range(len(res_json)):
        assert 'id' in res_json[item], "no id"
        assert res_json[item]["state"] == state, "Incorrect state"
        assert res_json[item]["brewery_type"] == brewery_type, "Incorrect brewery type"
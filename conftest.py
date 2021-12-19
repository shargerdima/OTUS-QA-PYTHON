import pytest


@pytest.fixture(scope="session")
def base_url_dog_api():
    return "https://dog.ceo/api"


@pytest.fixture(scope="session")
def base_url_openbrewerydb_api():
    return "https://api.openbrewerydb.org"


@pytest.fixture(scope="session")
def base_url_jsonplaceholder_api():
    return "https://jsonplaceholder.typicode.com"


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        default="https://ya.ru",
        help="It is request url"
    )

    parser.addoption(
        "--status_code",
        default="200",
        choices=["200", "201", "404"],
        help="It is status_code"
    )


@pytest.fixture
def base_url(request):
    return request.config.getoption("--url")


@pytest.fixture
def status_code(request):
    return request.config.getoption("--status_code")

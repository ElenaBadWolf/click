import pytest
from fixture.application import Application


@pytest.fixture
def app(request):
    browser = request.config.getoption("--browser")
    base_url = request.config.getoption("--baseUrl")
    fixture=Application(browser= browser, base_url = base_url)
    request.addfinalizer(fixture.destroy)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default = "chrome")
    parser.addoption("--baseUrl", action="store", default = "https://ssp.clickadu.com/#/app/auth/signUp")
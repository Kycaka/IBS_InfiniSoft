import pytest
from selenium import webdriver

from api_client.api_reqres import ApiClient


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.fixture(scope="function")
def api_calling():
    return ApiClient

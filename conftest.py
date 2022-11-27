import pytest
from selene.support.shared import browser


@pytest.fixture(scope="session")
def set_size_browser():
    browser.config.window_width = 300
    browser.config.window_height = 100


@pytest.fixture()
def open_browser():
    browser.open('https://google.ru')

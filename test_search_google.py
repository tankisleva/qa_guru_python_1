from selene.support.shared import browser
from selene import be, have


def test_google_positive(set_size_browser, open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene github').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_google_negative(set_size_browser, open_browser):
    browser.element('[name="q"]').should(be.blank).type('ekjtjtohjthet').press_enter()
    browser.element('[class="card-section"]').should(have.text('Your search - ekjtjtohjthet - did not match any documents.'))

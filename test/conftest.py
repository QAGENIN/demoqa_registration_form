import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse= True)
def browser_setting():
    browser.config.window_width = 1600
    browser.config.window_height = 1200
    browser.config.base_url = 'https://demoqa.com'

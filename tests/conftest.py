import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='function', autouse= True)
def browser_management():
    chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument('--headless')
    browser.config.driver_options = chrome_options
    browser.config.window_width = 1600
    browser.config.window_height = 900
    browser.config.base_url = 'https://demoqa.com'
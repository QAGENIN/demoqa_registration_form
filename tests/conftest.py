import logging

import pytest
from selene import browser, Browser, Config
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from tests.utils import attach


@pytest.fixture(scope='function')
def browser_setup():
    logging.basicConfig(level=logging.DEBUG)
    logging.info('Retrieving browser from 192.168.0.101:4445')
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": '113.0',
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor='http://test:test-password@192.168.0.101:4445/wd/hub',
        options=options
    )

    browser = Browser(Config(driver=driver))

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()

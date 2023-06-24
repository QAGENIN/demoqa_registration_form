import allure
import pytest
from allure_commons.types import AttachmentType
from selene import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser_setup():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": '113.0',
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor='http://172.17.0.1:4444/wd/hub',
        options=options,
    )

    browser.config.driver = driver

    yield fail_test_screen()


def fail_test_screen():
    if not pytest.ExitCode.OK:
        png = browser.driver.get_screenshot_as_png()
        allure.attach(
            body=png,
            name='screenshot',
            attachment_type=AttachmentType.PNG,
            extension='.png',
        )
    else:
        browser.quit()

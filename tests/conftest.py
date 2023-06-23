import pytest
from selene import Browser, Config, browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils import attach


@pytest.fixture(scope='function')
def browser_setup():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": '100.0',
        "selenoid:options": {"enableVNC": True, "enableVideo": True},
    }
    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor='https://user1:1234@selenoid.autotests.cloud/wd/hub',
        options=options
    )

    browser.config.driver = driver

    yield browser

    def pytest_sessionfinish(session, exitstatus):
        if exitstatus == pytest.ExitCode.TESTS_FAILED:
            attach.add_screenshot(browser)
            attach.add_logs(browser)
            attach.add_video(browser)

    browser.quit()

import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from demo_qa.utils import attach

load_dotenv()


@pytest.fixture(scope='function')
def setup_browser():
    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }

    options.capabilities.update(selenoid_capabilities)

    driver = webdriver.Remote(
        command_executor=os.getenv('SELENOID_URL'),
        options=options
    )

    browser.config.driver = driver
    browser.config.base_url = os.getenv('DEMO_QA_BASE_URL')

    yield browser

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)

    browser.quit()

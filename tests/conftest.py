import glob
import os

import pytest
from dotenv import load_dotenv
from selene.support.shared import browser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from demo_qa.utils import attach

load_dotenv()

path_output_files = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'resources')


@pytest.fixture()
def clear_dir():
    """Fixture: delete all files from dir with archive"""
    all_files = os.path.join(path_output_files, '*.*')
    for file in glob.glob(all_files):
        os.remove(file)


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

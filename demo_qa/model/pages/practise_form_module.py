from demo_qa.model.controls.radio import Radio
from demo_qa.utils import remove_ads
from selene import have
from selene.support.shared import browser


def open_page():
    browser.open('/automation-practice-form')
    browser.driver.maximize_window()
    remove_ads.remove_junk_ads(browser)


def add_name_and_surname(user):
    browser.element('#firstName').type(user.first_name)
    browser.element('#lastName').type(user.last_name)


def add_contacts(user):
    browser.element('#userEmail').type(user.email)
    browser.element('#userNumber').type(user.mobile)
    browser.element('#currentAddress').type(user.address)


def submit():
    browser.element('#submit').press_enter()


def choose_gender(user):
    Radio.radio_button('[name=gender]', user.gender)


def click(locator):
    browser.element(locator).click()


def check_validation_email():
    browser.element('#userEmail') \
        .should(have.css_property('border-color', value='rgb(40, 167, 69)'))


def check_invalid_controls(control):
    value = 'rgb(220, 53, 69)'

    browser.element(control) \
        .should(have.css_property('border-color', value=value))

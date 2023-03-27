import allure
import pytest
from allure_commons.types import Severity

from demo_qa.app import form
from demo_qa.data.user_data import test_user
from demo_qa.model.pages import form_module


@allure.label('owner', 'kudaev.m')
@allure.severity(Severity.NORMAL)
@allure.tag('web')
@allure.feature('Successful completion of the form')
@pytest.mark.parametrize('screen_size', ["1280x720", "1920x1080"])
def test_submitting_form_successfully(setup_browser, screen_size):
    width, height = screen_size.split('x')
    setup_browser.config.window_width = int(width)
    setup_browser.config.window_height = int(height)

    with allure.step('Open demoqa'):
        form.open_page()

    with allure.step('Fill form'):
        form.submit_form(test_user)

    with allure.step('Check that the form data is in the resulting table'):
        form.validate_form(test_user)


@allure.label('owner', 'kudaev.m')
@allure.severity(Severity.NORMAL)
@allure.tag('web')
@allure.feature('Successful completion of the form with only required fields')
def test_fill_only_required_fields(setup_browser):
    with allure.step('Open demoqa'):
        form.open_page()

    with allure.step('Fill main fields'):
        form.add_name_and_surname(test_user) \
            .choose_gender(test_user) \
            .add_contacts(test_user) \
            .submit()

    with allure.step('Check the filled data'):
        form.check_data(test_user.first_name) \
            .check_data(test_user.last_name) \
            .check_data(test_user.gender) \
            .check_data(test_user.mobile) \
            .check_data(test_user.email) \
            .check_data(test_user.address)


@allure.label('owner', 'kudaev.m')
@allure.severity(Severity.NORMAL)
@allure.tag('web')
@allure.feature('Check validation count numbers less then ten')
def test_validation_count_numbers_less_than_ten(setup_browser):
    with allure.step('Open demoqa'):
        form.open_page()

    with allure.step('Fill main fields and 9x number phone'):
        form.add_name_and_surname(test_user) \
            .choose_gender(test_user) \
            .add_contacts(test_user) \
            .submit()

    with allure.step('Check validation field'):
        form.check_validation_phone_number()


@allure.label('owner', 'kudaev.m')
@allure.severity(Severity.NORMAL)
@allure.tag('web')
@allure.feature('Check validation email field')
def test_validation_field_email(setup_browser):
    with allure.step('Open demoqa'):
        form_module.open_page()

    with allure.step('Fill main fields and email without @'):
        form_module.add_name_and_surname(test_user) \
            .choose_gender(test_user) \
            .add_contacts(test_user) \
            .submit()

    with allure.step('Check validation field email'):
        form_module.check_validation_email()


@allure.label('owner', 'kudaev.m')
@allure.severity(Severity.NORMAL)
@allure.tag('web')
@allure.feature('Send empty form')
def test_send_empty_form(setup_browser):
    with allure.step('Open demoqa'):
        form_module.open_page()

    with allure.step('Send empty form'):
        form_module.submit()

    with allure.step('Check validation on the form'):
        form_module.check_invalid_controls(control='#firstName')
        form_module.check_invalid_controls(control='#lastName')
        form_module.check_invalid_controls(control='#userNumber')

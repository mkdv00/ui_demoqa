import allure
from allure_commons.types import Severity

from demo_qa.data.user_data import test_user
from demo_qa.model.pages.practise_form import Form


def test_submitting_form_successfully():
    allure.dynamic.tag('web')
    allure.dynamic.severity(Severity.NORMAL)
    allure.dynamic.label('owner', 'kudaev.m')
    allure.dynamic.feature('Successful completion of the form')

    with allure.step('Open demoqa'):
        form = Form()
        form.open_page()

    with allure.step('Fill form'):
        form.submit_form(test_user)

    with allure.step('Check that the form data is in the resulting table'):
        form.validate_form(test_user)

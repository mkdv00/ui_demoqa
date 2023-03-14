from selene import have
from selene.support.shared import browser

from demo_qa.data.user_data import User
from demo_qa.model.controls.checkbox import Checkbox
from demo_qa.model.controls.dropdown import Dropdown
from demo_qa.model.controls.option_select import Select
from demo_qa.model.controls.radio import Radio
from demo_qa.utils import remove_ads
from demo_qa.utils import work_with_path


class Form:

    def __int__(self, user: User):
        self.user = user

    def validation(self, *args):
        browser.element('.table').all('td').even.should(have.texts(args))
        return self

    def open_page(self):
        browser.open('/automation-practice-form')
        browser.driver.maximize_window()
        remove_ads.remove_junk_ads(browser)
        return self

    def add_name_and_surname(self, user):
        browser.element('#firstName').type(user.first_name)
        browser.element('#lastName').type(user.last_name)
        return self

    def add_contacts(self, user):
        browser.element('#userEmail').type(user.email)
        browser.element('#userNumber').type(user.mobile)
        browser.element('#currentAddress').type(user.address)
        return self

    def add_subject(self, user):
        browser.element('#subjectsInput').type(user.subject).press_enter()
        return self

    def choose_hobby(self, user):
        Checkbox.click_checkbox('[for^=hobbies-checkbox]', user.hobby)
        return self

    def add_state(self, user):
        Dropdown.choose('#state', user.state)
        return self

    def add_city(self, user):
        Dropdown.choose('#city', user.city)
        return self

    def submit(self):
        browser.element('#submit').press_enter()
        return self

    def choose_gender(self, user):
        Radio.radio_button('[name=gender]', user.gender)
        return self

    def select_month(self, user):
        browser.element('.react-datepicker__month-select').click()
        Select.select_by_text('.react-datepicker__month-select', user.birth_month)
        return self

    def select_year(self, user):
        browser.element('.react-datepicker__year-select').click()
        Select.select_by_text('.react-datepicker__year-select', user.birth_year)
        return self

    def select_day(self, user):
        browser.element(f'.react-datepicker__day--0{user.birth_day}').click()
        return self

    def send_file(self):
        path = work_with_path.get_path('resources/photo.jpg')
        browser.element('#uploadPicture').set_value(path)
        return self

    def click(self, locator):
        browser.element(locator).click()
        return self

    def add_birthday(self, user):
        self.click('#dateOfBirthInput')
        self.select_month(user)
        self.select_year(user)
        self.select_day(user)
        return self

    def submit_form(self, user):
        self.add_name_and_surname(user)
        self.add_contacts(user)
        self.choose_gender(user)
        self.add_birthday(user)
        self.add_subject(user)
        self.choose_hobby(user)
        self.send_file()
        self.add_state(user)
        self.add_city(user)
        self.submit()

    def validate_form(self, user):
        user_birth = f'{user.birth_day} {user.birth_month},{user.birth_year}'
        user_full_name = user.first_name + ' ' + user.last_name
        user_place = user.state + ' ' + user.city

        self.validation(
            user_full_name,
            user.email,
            user.gender,
            user.mobile,
            user_birth,
            user.subject,
            user.hobby,
            '',
            user.address,
            user_place
        )

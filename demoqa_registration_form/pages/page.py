from demoqa_registration_form.users_data.users import student, User
from selene import browser, have, be
import os


class RegistrationPage:
    def __init__(self):
        self.endpoint = '/automation-practice-form'

    def open(self):
        browser.open(self.endpoint)

    def fill_first_name(self, value):
        browser.element('[id="firstName"]').send_keys(value)

    def fill_last_name(self, value):
        browser.element('[id="lastName"]').send_keys(value)

    def fill_email(self, value):
        browser.element('[id="userEmail"]').send_keys(value)

    def pick_gender(self, value):
        browser.element(f'[name="gender"][value={value}]').double_click()

    def fill_phone(self, value):
        browser.element('[id="userNumber"]').send_keys(value)

    def date_of_birth_input(self, day, month, year):
        browser.element('#dateOfBirthInput').click()
        browser.execute_script('document.getElementById("dateOfBirthInput").value = ""')
        browser.element('#dateOfBirthInput').send_keys(f'{day} {month} {year}').press_enter()

    def fill_subjects(self, value):
        browser.element('#subjectsInput').click().send_keys(value).press_enter()

    def choose_hobby(self, value):
        browser.all('.custom-control-label').element_by(have.exact_text(value)).click()

    def upload_pic(self, pic):
        browser.element('#uploadPicture').send_keys(os.getcwd() + f"/resources/{pic}")

    def fill_current_adress(self, value):
        browser.element('[id="currentAddress"]').send_keys(value)

    def select_state(self, value):
        browser.element('#state #react-select-3-input').type(value).press_enter()

    def select_city(self, value):
        browser.element('#city #react-select-4-input').type(value).press_enter()

    def submit_form(self):
        browser.execute_script('document.getElementById("submit").click()')

    def assert_form_submission_text(self, expected_text):
        browser.element('#example-modal-sizes-title-lg').should(have.text(expected_text))

    def assert_user_data(self, student: User):
        full_name = f'{student.first_name} {student.last_name}'
        full_birthday = f'{student.date_of_birth[0]} {student.date_of_birth[1]},{student.date_of_birth[2]}'
        expected_values = [
            f'Student Name {full_name}',
            f'Student Email {student.email}',
            f'Gender {student.gender}',
            f'Mobile {student.phone_number}',
            f'Date of Birth {full_birthday}',
            f'Subjects {student.subject}',
            f'Hobbies {student.hobby}',
            f'Picture {student.picture_file}',
            f'Address {student.address}',
            f'State and City {student.state} {student.city}'
        ]

    def register(self, student: User):
        self.fill_first_name('Test')
        self.fill_last_name('Test')
        self.fill_email('test@test.com')
        self.pick_gender('Male')
        self.fill_phone('1234567891')
        self.date_of_birth_input(24, 'August', 1994)
        self.fill_subjects('Maths')
        self.choose_hobby('Sports')
        self.upload_pic('test.png')
        self.fill_current_adress('Test-city, test street, test house 2')
        self.select_state('NCR')
        self.select_city('Delphi')
        self.submit_form()

    def should_have_registered(self, student: User):
        self.assert_user_data(student)

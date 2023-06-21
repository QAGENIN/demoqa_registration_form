from demoqa_registration_form.users_data.users import student, User
from selene import browser, have, be
import os
import allure

class RegistrationPage:
    @allure.step('Открываем страницу')
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')
    @allure.step('Вводим имя')
    def fill_first_name(self, value):
        browser.element('[id="firstName"]').send_keys(value)
    @allure.step('Вводим фамилию')
    def fill_last_name(self, value):
        browser.element('[id="lastName"]').send_keys(value)

    @allure.step('Вводим email')
    def fill_email(self, value):
        browser.element('[id="userEmail"]').send_keys(value)

    @allure.step('Выбираем гендер')
    def pick_gender(self, value):
        browser.element(f'[name="gender"][value={value}]').double_click()

    @allure.step('Вводим номер телефона')
    def fill_phone(self, value):
        browser.element('[id="userNumber"]').send_keys(value)

    @allure.step('Заполняем дату рождения')
    def date_of_birth_input(self, date_of_birth):
        day, month, year = date_of_birth
        browser.element('#dateOfBirthInput').click()
        browser.execute_script('document.getElementById("dateOfBirthInput").value = ""')
        browser.element('#dateOfBirthInput').send_keys(f'{day} {month} {year}').press_enter()

    @allure.step('Выбираем предметы')
    def fill_subjects(self, value):
        browser.element('#subjectsInput').click().send_keys(value).press_enter()

    @allure.step('Выбираем хобби')
    def choose_hobby(self, value):
        browser.all('.custom-control-label').element_by(have.exact_text(value)).click()

    @allure.step('Загружаем картинку')
    def upload_pic(self, pic):
        browser.element('#uploadPicture').send_keys(os.getcwd() + f"/resources/{pic}")

    @allure.step('Вводим адресс')
    def fill_current_adress(self, value):
        browser.element('[id="currentAddress"]').send_keys(value)

    @allure.step('Выбираем штат')
    def select_state(self, value):
        browser.element('#state #react-select-3-input').type(value).press_enter()

    @allure.step('Выбираем город')
    def select_city(self, value):
        browser.element('#city #react-select-4-input').type(value).press_enter()

    @allure.step('Нажимаем кнопку submit')
    def submit_form(self):
        browser.execute_script('document.getElementById("submit").click()')

    @allure.step('Проверяем правильность заполнения формы')
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
        browser.all('tbody tr').should(have.exact_texts(*expected_values))

    def register(self, student: User):
        self.fill_first_name(student.first_name)
        self.fill_last_name(student.last_name)
        self.fill_email(student.email)
        self.pick_gender(student.gender)
        self.fill_phone(student.phone_number)
        self.date_of_birth_input(student.date_of_birth)
        self.fill_subjects(student.subject)
        self.choose_hobby(student.hobby)
        self.upload_pic(student.picture_file)
        self.fill_current_adress(student.address)
        self.select_state(student.state)
        self.select_city(student.city)
        self.submit_form()

    def should_have_registered(self, student: User):
        self.assert_user_data(student)

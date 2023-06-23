import allure
from demoqa_registration_form.users_data.users import student
from selene import browser, have
import os


class RegistrationPage:
    def open(self):
        browser.open('https://demoqa.com/automation-practice-form')

    def first_name_filled(self):
        return browser.element('[id="firstName"]')

    def last_name_filled(self):
        return browser.element('[id="lastName"]')

    def email_filled(self):
        return browser.element('[id="userEmail"]')

    def gender_picked(self):
        return browser.element(f'[name="gender"][value=Male]')

    def phone_filled(self):
        return browser.element('[id="userNumber"]')

    def date_of_birth_filled(self, date_of_birth):
        day, month, year = date_of_birth
        browser.element('#dateOfBirthInput').click()
        browser.execute_script('document.getElementById("dateOfBirthInput").value = ""')
        browser.element('#dateOfBirthInput').send_keys(
            f'{day} {month} {year}'
        ).press_enter()

    def subjects_filled(self):
        return browser.element('#subjectsInput')

    def hobby_chooised(self):
        return browser.all('.custom-control-label')

    def upload_pic(self):
        return browser.element('#uploadPicture')

    def current_adress_filled(self):
        return browser.element('[id="currentAddress"]')

    def state_selected(self):
        return browser.element('#state #react-select-3-input')

    def city_selected(self):
        return browser.element('#city #react-select-4-input')

    def submit_form(self):
        browser.execute_script('document.getElementById("submit").click()')

    def assert_user_data(self):
        date_of_birth = f"{student.get('date_of_birth')[0]} {student.get('date_of_birth')[1]},{student.get('date_of_birth')[2]}"
        expected_values = [
            f"Student Name {student.get('first_name')} {student.get('last_name')}",
            f"Student Email {student.get('email')}",
            f"Gender {student.get('gender')}",
            f"Mobile {student.get('phone_number')}",
            f"Date of Birth {date_of_birth}",
            f"Subjects {student.get('subject')}",
            f"Hobbies {student.get('hobby')}",
            f"Picture {student.get('picture_file')}",
            f"Address {student.get('address')}",
            f"State and City {student.get('state')} {student.get('city')}",
        ]
        browser.all('tbody tr').should(have.exact_texts(*expected_values))

    @allure.step('Заполнение формы регистрации')
    def register(self):
        with allure.step(f"заполняем поле имя - {student.get('first_name')}"):
            self.first_name_filled().send_keys(student.get('first_name'))

        with allure.step(f"заполняем поле имя - {student.get('last_name')}"):
            self.last_name_filled().send_keys(student.get('last_name'))

        with allure.step(f"заполняем поле email - {student.get('email')}"):
            self.email_filled().send_keys(student.get('email'))

        with allure.step(f"выбираем гендер - {student.get('gender')}"):
            self.gender_picked().double_click()

        with allure.step(
            f"заполняем поле номер телефона - {student.get('phone_number')}"
        ):
            self.phone_filled().send_keys(student.get('phone_number'))

        with allure.step(f"выбираем дату рождения - {student.get('date_of_birth')}"):
            self.date_of_birth_filled(student.get('date_of_birth'))

        with allure.step(f"заполняем поле subject - {student.get('subject')}"):
            self.subjects_filled().click().send_keys(
                student.get('subject')
            ).press_enter()

        with allure.step(f"выбираем хобби - {student.get('hobby')}"):
            self.hobby_chooised().element_by(have.exact_text('Sports')).click()

        with allure.step(f"загружаем картинку - {student.get('picture_file')}"):
            self.upload_pic().send_keys(
                os.getcwd() + f"/resources/{student.get('picture_file')}"
            )
        with allure.step(f"заполняем адрес - {student.get('address')}"):
            self.current_adress_filled().send_keys(student.get('address'))

        with allure.step(f"выбираем штат - {student.get('state')}"):
            self.state_selected().type(student.get('state')).press_enter()

        with allure.step(f"выбираем город - {student.get('city')}"):
            self.city_selected().type(student.get('city')).press_enter()

        with allure.step('нажимаем кнопку подтвердить'):
            self.submit_form()

    @allure.step('Проверка заполнения формы')
    def should_have_registered(self):
        self.assert_user_data()

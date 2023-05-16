from selene import browser, have, be
import os
from tests import resources


def test_homework():
    browser.open('/automation-practice-form')
    browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.5)"')

    browser.element('[id="firstName"]').send_keys('Test')
    browser.element('[id="lastName"]').send_keys('Test')
    browser.element('[id="userEmail"]').send_keys('test@test.com')
    browser.element('[name="gender"][value=Male]').double_click()
    browser.element('[id="userNumber"]').send_keys('1234567891')

    browser.element('[id="dateOfBirthInput"]').click()
    browser.element('.react-datepicker__year-select').click().element('[value="1994"]').click()
    browser.element('.react-datepicker__month-select').click().element('[value="7"]').click()
    browser.element('.react-datepicker__day--024').click()

    browser.element('#subjectsInput').click().send_keys('Maths').press_enter()

    browser.element('label[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath((os.path.dirname(__file__) + '/resources/test.png')))

    browser.element('[id="currentAddress"]').send_keys('Test-city, test street, test house 2')

    browser.element('#state').click()
    browser.all('[id^=react-select][id*=option]').element_by(have.exact_text('NCR')).click()
    browser.element('#react-select-4-input').type('Delhi').press_enter()

    browser.element('#submit').press_enter()

    browser.all('tbody tr').should(have.exact_texts(
        'Student Name Test Test', 'Student Email test@test.com', 'Gender Male', 'Mobile 1234567891',
        'Date of Birth 24 August,1994', 'Subjects Maths', 'Hobbies Sports',
        'Picture test.png', 'Address Test-city, test street, test house 2',
        'State and City NCR Delhi'))

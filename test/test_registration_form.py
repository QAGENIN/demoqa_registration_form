from demoqa_registration_form.pages.page import RegistrationPage

registration_page = RegistrationPage()


def test_registration_page(browser_setting):
    registration_page.open()

    #  WHEN
    registration_page.fill_first_name('Test')
    registration_page.fill_last_name('Test')
    registration_page.fill_email('test@test.com')
    registration_page.pick_gender('Male')
    registration_page.fill_phone('1234567891')

    registration_page.date_of_birth_input(24, 'August', 1994)

    registration_page.fill_subjects('Maths')
    registration_page.choose_hobby('Sports')

    registration_page.upload_pic('test.png')
    registration_page.fill_current_adress('Test-city, test street, test house 2')

    registration_page.select_state('NCR')
    registration_page.select_city('Delphi')

    registration_page.submit_form()

    # THEN
    registration_page.assert_form_submission_text()
    registration_page.assert_user_data(
        'Student Name Test Test',
        'Student Email test@test.com',
        'Gender Male',
        'Mobile 1234567891',
        'Date of Birth 24 August,1994',
        'Subjects Maths',
        'Hobbies Sports',
        'Picture test.png',
        'Address Test-city, test street, test house 2',
        'State and City NCR Delhi')

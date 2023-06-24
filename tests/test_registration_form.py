from demoqa_registration_form.pages.registration_page import RegistrationPage

registration_page = RegistrationPage()


def test_registration_page(browser_setup, fail_test_screen):
    registration_page.open()

    registration_page.register()

    registration_page.should_have_registered()

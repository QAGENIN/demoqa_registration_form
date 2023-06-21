from demoqa_registration_form.pages.page import RegistrationPage
from demoqa_registration_form.users_data.users import student

registration_page = RegistrationPage()


def test_registration_page(browser_setup):

    registration_page.open()

    registration_page.register(student)

    registration_page.should_have_registered(student)

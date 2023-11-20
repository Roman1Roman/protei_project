from pages.mobile_operators_page import MobileOperators, MainPage
import allure
main_page = MainPage()
mob_oper_page = MobileOperators()

@allure.title('Filling an application on mobile operators page starting from main page')
@allure.tag('Frontend')
def test_filling_table_mob_oper_page():
    #with allure.step('Opening main page'):
        #main_page.open_main_page()

    with allure.step('Move to mobile operator page'):
        mob_oper_page.open_mobile_operator_page()
    with allure.step('Click on leave an application'):
        mob_oper_page.leave_application()
    with allure.step('Filling fields in table'):
        mob_oper_page.filling_form()

    with allure.step('click on submit button'):
        mob_oper_page.submit_sending()
    with allure.step('Checking for sending an application'):
        mob_oper_page.check_sending()

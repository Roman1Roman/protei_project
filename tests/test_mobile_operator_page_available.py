from pages.mobile_operators_page import MobileOperators, MainPage
import allure
main_page = MainPage()
mob_oper_page = MobileOperators()

@allure.title('Checking mobile operators page')
@allure.tag('Frontend')
def test_opening_mobile_operator_page(browser_manage):
    with allure.step('Open main page'):
        main_page.open_main_page()
    with allure.step('Move to mobile operator page'):
        mob_oper_page.open_mobile_operator_page()

    with allure.step('Checking for info on page (for available)'):
        mob_oper_page.checking_for_available()


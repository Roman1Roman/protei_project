from pages.unicom_page import MainPage, UnicomPage
import allure
main_page = MainPage()
unicom_page = UnicomPage()

@allure.title('Checking unicom page')
@allure.tag('Frontend')
def test_opening_mobile_operator_page(browser_manage):
    with allure.step('Open main page'):
        main_page.open_main_page()
    with allure.step('Move to unicom page'):
        unicom_page.open_unicom_page()

    with allure.step('Checking for info on page (for available)'):
        unicom_page.check_available_page()
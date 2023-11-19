from pages.unicom_page import MainPage, UnicomPage
import allure
main_page = MainPage()
unicom_page = UnicomPage()

@allure.title('Filling an application on unicom page')
@allure.tag('Frontend')
def test_filling_table_mob_oper_page(browser_manage):
    with allure.step('Opening main page'):
        main_page.open_main_page()
    with allure.step('Move to unicom page'):
        unicom_page.open_unicom_page()
    with allure.step('Click on create an application button'):
        unicom_page.leave_application_unicom()

    with allure.step('Filling form on unicom page'):
        unicom_page.filling_form_unicom()
    with allure.step('Click on send application button'):
        unicom_page.click_submit_button_unicom()

    with allure.step('Check page text after submitting'):
        unicom_page.check_for_submitting()
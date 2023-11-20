from pages.main_page import MainPage
import allure
main_page = MainPage()

@allure.title('Checking main page')
@allure.tag('Frontend')
def test_opening_main_page():
    #with allure.step('Opening browser page protei.ru'):
        #main_page.open_main_page()

    with allure.step('Checking text on main page'):
        main_page.should_have_text()


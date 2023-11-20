import allure
from selene import be, have, command
from selene.support.shared import browser
from pages.main_page import MainPage


class MobileOperators:
    '''class for description mobile operators page'''
    leave_an_application = "//a[@href= '#block-contacts-modal' and text()= 'Оставить заявку']"
    table_full = '#webform-submission-obratnaya-svyaz-block-content-17-add-form'
    table_name = '#edit-name--3'
    table_number = '#edit-phone--3'
    table_mail = '#edit-mail--3'
    table_message = '#edit-message--2'
    check_box_true = '#edit-fz152-agreement--3'
    send_application = '#edit-actions-submit--3'
    page_elements_required = '//h2[@class="paragraph-title-text-file__title"]'
    sent_element = '//div[@class="region-content"]'

    def open_mobile_operator_page(self):
        browser.open()
        browser.element(MainPage.to_mobile_operators).click()

    def leave_application(self):
        browser.element(MobileOperators.leave_an_application).click()

    def filling_form(self):
        with allure.step('filling name'):
            browser.element(MobileOperators.table_name).type('Fedya')
        with allure.step('filling number'):
            browser.element(MobileOperators.table_number).type('88005553535')
        with allure.step('filling email'):
            browser.element(MobileOperators.table_mail).type('dog@mail.ru')
        with allure.step('filling message'):
            browser.element(MobileOperators.table_message).type('Using for tests, sorry')
        with allure.step('click on checkbox'):
            browser.element(MobileOperators.check_box_true).perform(command.js.click)


    def submit_sending(self):
        with allure.step('click on send button'):
            browser.element(MobileOperators.send_application).click()

    def checking_for_available(self):
        browser.element(MobileOperators.page_elements_required).should(have.text("Решения для мобильных сетей"))

    def check_sending(self):
        browser.element(MobileOperators.sent_element).should(have.text('Мы получили ваше обращение'))

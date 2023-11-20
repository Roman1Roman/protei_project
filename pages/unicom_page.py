import allure
from selene import be, have, command
from selene.support.shared import browser
from pages.main_page import MainPage


class UnicomPage:
    """class for description unicom page of protei"""
    available_text_element = '//div[@class="paragraph-title-text-file__field-text"]'
    application_button = '//a[@href="#block-order" and text()= "Оставить заявку"]'
    form_name = '#edit-name--2'
    form_number = '#edit-phone--2'
    form_email = '#edit-mail--2'
    form_message = '#edit-comment'
    form_checkbox = '#edit-fz152-agreement--2'
    form_submit_button = '#edit-actions-submit--2'
    sent_message_text = '//div[@class="node-page-full__body-item"]'

    def open_unicom_page(self):
        with allure.step('Opening necessary page'):
            browser.open()
            browser.element(MainPage.to_unicom).click()

    def check_available_page(self):
        with allure.step('Checking info on the page'):
            browser.element(UnicomPage.available_text_element).should(
                have.text('Платформа унифицированных коммуникаций (Unified Communications) ПРОТЕЙ-Юником'))

    def leave_application_unicom(self):
        with allure.step('Click on create an application button'):
            browser.element(UnicomPage.application_button).click()

    def filling_form_unicom(self):
        with allure.step('filling name'):
            browser.element(UnicomPage.form_name).type('Fedya')
        with allure.step('filling number'):
            browser.element(UnicomPage.form_number).type('88005553535')
        with allure.step('filling email'):
            browser.element(UnicomPage.form_email).type('dog@mail.ru')
        with allure.step('filling message'):
            browser.element(UnicomPage.form_message).type('Using for tests, sorry')
        with allure.step('click on checkbox'):
            browser.element(UnicomPage.form_checkbox).perform(command.js.click)

    def click_submit_button_unicom(self):
        with allure.step('click on the send application button'):
            browser.element(UnicomPage.form_submit_button).click()

    def check_for_submitting(self):
        with allure.step('Check text on page after submitting'):
            browser.element(UnicomPage.sent_message_text).should(have.text('Спасибо за обращение, ваша заявка успешно'))

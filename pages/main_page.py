import os

from selene import be, have
from selene.support.shared import browser


class MainPage:
    '''class for description main page'''
    content_main_page = "//span[text()='ПРОТЕЙ']"
    to_mobile_operators = "//a[@href='https://protei.ru/solutions/mobile' and text()= 'Мобильным операторам']"
    to_unicom = "//a[@href='https://protei.ru/products/protei-uc' and text()= 'Корпоративный мессенджер']"

    def open_main_page(self):
        return browser.open('https://protei.ru/')

    def should_have_text(self):
        return browser.element('//h1[@class="block-content-front-titr-full__field-title"]').should(have.text('Научно-Технический Центр ПРОТЕЙ'))

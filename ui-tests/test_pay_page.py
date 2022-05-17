from pages.pay_page import PayPage
import pytest


class TestPayPage:
    def test_check_page_elements(self, browser, link):  # RTM-91 Проверка элементов платежной страницы покупателя
        PayPage(browser, link)\
            .open()\
            .check_page_elements()\
            .check_order_elements()

    def test_check_card_number_input(self, browser, link):  # RTM-92 Проверка поля ввода номера карты
        PayPage(browser, link)\
            .check_card_number_input()

    def test_check_card_date_input(self, browser, link):  # RTM-93 Проверка поля ввода срока действия карты
        PayPage(browser, link)\
            .check_card_date_input()

    def test_check_cvc_input(self, browser, link):  # RTM-94 Проверка поля ввода CVC
        PayPage(browser, link)\
            .check_cvc_input()

    def test_check_mail_input(self, browser, link):  # RTM-95 Проверка поля ввода адреса
        PayPage(browser, link)\
        .check_mail_input()

    def test_check_pay_button(self, browser, link):  # RTM-96 Проверка активации кнопки "Оплатить"
        PayPage(browser, link)\
            .open()\
            .check_pay_button()\
            .click_pay_button()

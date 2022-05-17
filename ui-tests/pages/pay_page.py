from .base_function import BaseFunction
from .locators import PayPageLocators


class PayPage(BaseFunction):
    def check_page_elements(self):
        elem = [PayPageLocators.CVC,
                PayPageLocators.MAIL,
                PayPageLocators.CARD_DATE,
                PayPageLocators.CARD_NUMBER,
                PayPageLocators.INPUT_CARD_DATA_TXT,
                PayPageLocators.ORDER_BASKET]
        self.check_elements(elem)
        return self

    def check_order_elements(self):
        elem = [PayPageLocators.ORDER_SUMM,
                PayPageLocators.ORDER_ELEMENTS_TXT,
                PayPageLocators.PAY_BUTTON]
        self.check_elements(elem)
        return self

    def __check_variants(self, locator, variants):
        for item in variants:
            self.send_value_by_locator(item[0], locator)
            self.check_input_field(PayPageLocators.CARD_NUMBER, item[1])

    def check_card_number_input(self):
        variants = [["Text", ""], ["  ", ""], ["№%?*()!\/.,}{[]", ""], ["1234", "1234"],
                    ["Text", "1234"], ["   ", "1234"], ["№%?*()!\/.,}{[]", "1234"],
                    ["5678912345678", "12345678912345678"]]
        self.__check_variants(PayPageLocators.CARD_NUMBER, variants)

    def check_card_date_input(self):
        variants = [["Text", ""], ["  ", ""], ["№%?*()!\/.,}{[]", ""], ["1220", ""], ["0224", "0224"]]
        self.__check_variants(PayPageLocators.CARD_DATE, variants)

    def check_cvc_input(self):
        variants = [["Text", ""], ["  ", ""], ["№%?*()!\/.,}{[]", ""], ["123", "123"]]
        self.__check_variants(PayPageLocators.CVC, variants)

    def check_mail_input(self):
        variants = [["Это поле ввода адреса 1234!'№?*(", "Это поле ввода адреса 1234!'№?*("]]
        self.__check_variants(PayPageLocators.MAIL, variants)

    def __check_is_pay_button_active(self, result):
        assert self.is_element_clickable_by_locator(PayPageLocators.PAY_BUTTON) == result, \
            f"Кнопка Оплатить не равна ожидаемому результату, assert - {result}!"

    def check_pay_button(self):
        self.__check_is_pay_button_active(False)
        self.send_value_by_locator("12345678912345678", PayPageLocators.CARD_NUMBER)
        self.__check_is_pay_button_active(False)
        self.send_value_by_locator("0224", PayPageLocators.CARD_DATE)
        self.__check_is_pay_button_active(False)
        self.send_value_by_locator("123", PayPageLocators.CVC)
        self.__check_is_pay_button_active(False)
        self.send_value_by_locator("Это поле ввода адреса 1234!'№?*(", PayPageLocators.MAIL)
        self.__check_is_pay_button_active(True)

    def click_pay_button(self):
        current_url = self.browser.current_url()
        self.click_element_by_locator(PayPageLocators.PAY_BUTTON)
        assert current_url != self.browser.current_url(), \
            "Не открылось модальное окно с сообщение об успешной/не успешной оплате!"

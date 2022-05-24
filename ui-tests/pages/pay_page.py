from .base_function import BaseFunction
from .locators import PayPageLocators
import time


class PayPage(BaseFunction):
    def check_page_elements(self):
        elem = [PayPageLocators.CVC,
                PayPageLocators.CARD_DATE_MONTH,
                PayPageLocators.CARD_DATE_YEAR,
                PayPageLocators.CARD_NUMBER,
                PayPageLocators.INPUT_CARD_DATA_TXT,
                PayPageLocators.PAY_BUTTON]
        self.check_elements(elem)
        return self


    def __check_variants(self, locator, variants):
        for item in variants:
            self.send_value_by_locator(item[0], locator)
            #time.sleep(1)
            self.check_input_field(locator, item[1])

    def check_card_number_input(self):
        variants = [["Text", ""], ["№%?*()!\/,}{[]", ""], ["1234", "1234"],
                    ["   ", "1234"], ["№%?*()!\/,}{[]", "1234"],
                    ["5678912345678", "12345678912345678"]]
        self.__check_variants(PayPageLocators.CARD_NUMBER, variants)

    def check_user_name_input(self):
        variants = [["Держатель карты 12435№)_%№", "Держатель карты 12435№)_%№"]]
        self.__check_variants(PayPageLocators.CARD_USER, variants)

    def check_card_month_input(self):
        variants = [["Text", ""], ["№%?*()!\/,}{[]", ""], ["1220", "12"]]
        self.__check_variants(PayPageLocators.MONTH, variants)
        return self

    def check_card_year_input(self):
        variants = [["Text", ""], ["№%?*()!\/,}{[]", ""], ["2022", "2022"]]
        self.__check_variants(PayPageLocators.YEAR, variants)
        return self

    def check_cvc_input(self):
        variants = [["Text", ""], ["№%?*()!\/,}{[]", ""], ["123", "123"]]
        self.__check_variants(PayPageLocators.CVC, variants)

    def __check_is_pay_button_active(self, result):
        assert self.is_element_clickable_by_locator(PayPageLocators.PAY_BUTTON) == result, \
            f"Кнопка Оплатить не равна ожидаемому результату, assert - {result}!"

    def check_pay_button(self):
        self.__check_is_pay_button_active(False)
        self.send_value_by_locator("12345678912345678", PayPageLocators.CARD_NUMBER)
        self.__check_is_pay_button_active(False)
        self.send_value_by_locator("02", PayPageLocators.CARD_DATE_MONTH)
        self.__check_is_pay_button_active(False)
        self.send_value_by_locator("12", PayPageLocators.CARD_DATE_YEAR)
        self.__check_is_pay_button_active(False)
        self.send_value_by_locator("123", PayPageLocators.CVC)
        self.__check_is_pay_button_active(True)

    def click_pay_button(self):
        current_url = self.browser.current_url()
        self.click_element_by_locator(PayPageLocators.PAY_BUTTON)
        assert current_url != self.browser.current_url(), \
            "Не открылось модальное окно с сообщение об успешной/не успешной оплате!"

    def check_success_page_elements(self):
        elem = [PayPageLocators.SUCCESS_MESSAGE_TXT,
                PayPageLocators.PAGE_BUTTON]
        self.check_elements(elem)

    def check_unsuccess_page_elements(self):
        elem = [PayPageLocators.UNSUCCESS_MESSAGE_TXT,
                PayPageLocators.PAGE_BUTTON]
        self.check_elements(elem)

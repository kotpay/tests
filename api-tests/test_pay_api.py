from api_base_function import BaseMethods
import unittest


class MyTestCase(unittest.TestCase, BaseMethods):
    def test_create_order(self):
        data = self.get_json_from_file("create_order.json")
        response = self.check_POST_response("/order/register.do", data=data).json()
        print(response)
        self.check_successes_response(response)

    def test_create_order_invalid_amount(self):
        data = self.create_custom_json_for_order("0", "RUB")
        response = self.check_POST_response("/order/register.do", data=data).json()
        print(response)
        self.check_response_error(response, "client.amount.invalid")

    def test_create_order_invalid_currency(self):
        data = self.create_custom_json_for_order("120", "RAB")
        response = self.check_POST_response("/order/register.do", data=data).json()
        print(response)
        self.check_response_error(response, "client.currency.invalid")

    def test_without_order(self):
        data = self.create_custom_json_for_pay("123", "1234567812345678", "12/23", "123", "Adiz Mukbilov")
        response = self.check_POST_response("/payment/card.do", data=data).json()
        self.check_response_error(response, "client.order.missing")

    def test_old_expiration(self):
        id = self.create_order()
        data = self.create_custom_json_for_pay(id, "1234567812345678", "202005", "123", "Adiz Mukbilov")
        response = self.check_POST_response("/payment/card.do", data=data).json()
        self.check_response_error(response, "client.expiration.invalid")

    def test_get_DEPOSITED_status(self):
        id = self.create_order()
        data = self.create_custom_json_for_pay(id, "1234567812345678", "202305", "123", "Adiz Mukbilov")
        response = self.check_POST_response("/payment/card.do", data=data).json()
        self.check_successes_response(response)
        self.assertEqual(response['data']['status'], 'DEPOSITED')

    def test_order_status(self):
        id = self.create_order()
        data = {"orderId": id}
        response = self.check_POST_response("/order/status.do", data=data).json()
        print(response)
        self.check_successes_response(response)
        self.assertEqual(response['data']['status'], 'CREATED')

    def open_success_pay_page(self):
        id = self.create_order()
        response = self.check_GET_response(f"https://skipperprivate.github.io/courseApp/?orderId={id}")
        self.check_successes_response(response)

    def open_fail_pay_page(self):
        response = self.check_GET_response(f"https://skipperprivate.github.io/courseApp/?orderId=")
        self.check_successes_response(response)


if __name__ == '__main__':
    unittest.main()

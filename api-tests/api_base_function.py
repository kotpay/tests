import json
import requests


class BaseMethods:
    def link(s):
        return "https://serene-inlet-14695.herokuapp.com/gateway"

    def get_json_from_file(s, file_name):
        with open(f"../jsons/{file_name}", "r") as read_file:
            return json.load(read_file)

    def check_GET_response(s, url, assertion_status_code=200):
        response = requests.get(s.link() + url)
        s.assertEqual(response.status_code, assertion_status_code)
        return response

    def check_POST_response(s, url, data, assertion_status_code=200):
        response = requests.post(s.link() + url, json=data)
        s.assertEqual(response.status_code, assertion_status_code)
        return response

    def check_response_error(s, response, assert_error):
        s.assertEqual(response['success'], False)
        s.assertEqual(response['error']['code'], assert_error)

    def check_successes_response(s, response):
        s.assertEqual(response['success'], True)

    def create_order(self):
        data = self.get_json_from_file("create_order.json")
        response = self.check_POST_response("/order/register.do", data=data).json()
        return response['data']['orderId']

    def create_custom_json_for_pay(s, orderId, pan, expiration, cvc, cardholder):
        file = {"orderId": orderId, "pan": pan,
                "expiration": expiration, "cvc": cvc,"cardholder": cardholder}
        return file

    def create_custom_json_for_order(s, amount, currency):
        file = {"amount": amount, "currency": currency,
                "returnUrl":  "order_id"}
        return file
from flask import Flask
import unittest
import requests

class FlaskTest(unittest.TestCase):
    test_header = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }

    url = "http://127.0.0.1:5000/checkout"
    # test response ok
    def test_response(self):
        r = requests.post(self.url, json=self.test_body_1)
        self.assertEqual(r.status_code, 200)
        print("Test response completed")
    
    # Example from the doc
    test_body_1 = ["001","002","001","004","003"]
    test_price_1 = 360
    def test_return_value_1(self):
        r = requests.post(self.url, json=self.test_body_1)
        self.assertEqual(r.json(), {"price":self.test_price_1})
        print("Passed example case")

    # no items 
    test_body_2 = []
    test_price_2 = 0
    def test_return_value_2(self):
        r = requests.post(self.url, json=self.test_body_2)
        self.assertEqual(r.json(), {"price":self.test_price_2})
        print("Passed empty case")

    # more items with multiple groups of discounts
    test_body_3 = ["001","002","001","004","003","001","002","002","002"]
    test_price_3 = 520

    def test_return_value_3(self):
        r = requests.post(self.url, json=self.test_body_3)
        self.assertEqual(r.json(), {"price":self.test_price_3})
        print("Passed multiple discounts case")
    
    # watch id not in catalogue
    test_body_4 = ["001","002","001","005"]
    def test_return_value_4(self):
        r = requests.post(self.url, json=self.test_body_4)
        self.assertEqual(r.status_code, 400)
        print("Handles wrong watch id's")


if __name__ == "__main__":
    tester = FlaskTest()
    tester.test_response()
    tester.test_return_value_1()
    tester.test_return_value_2()
    tester.test_return_value_3()
    tester.test_return_value_4()
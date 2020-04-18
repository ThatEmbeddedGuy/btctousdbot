import unittest
import requests
import rates
from httmock import all_requests, HTTMock


@all_requests
def mocked_data(url, request):
    return {'status_code': 200, 'content': b'{"mins":5,"price":"999"}'}


class TestRatesModule(unittest.TestCase):

    def test_on_mock_parse_answer(self):
        with HTTMock(mocked_data):
            self.assertEqual(rates.make_request("mocked"), "999")

    def test_empty_symbol(self):
        self.assertIsNone(rates.make_request(""))

    def test_getRatesConcurrent_default_returns_2_concurrency(self):
        self.assertEqual(len(rates.get_rates_concurrent()), 2)

    def test_getRatesConcurrent_invalidCurrency(self):
        self.assertEqual(rates.get_rates_concurrent(
            ["invalid"]), {'invalidUSDT': None})

    def test_getRatesConcurrent_mocked_data(self):
        with HTTMock(mocked_data):
            self.assertEqual(rates.get_rates_concurrent(
                ["mocked"]), {'mockedUSDT': "999"})


if __name__ == '__main__':
    unittest.main()

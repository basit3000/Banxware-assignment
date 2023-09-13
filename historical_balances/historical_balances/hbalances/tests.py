from django.test import TestCase, SimpleTestCase
from . views import Balances, Transactions, HistoricalBalancesList
from rest_framework.test import APITestCase, APIClient
import unittest, requests
from .serializers import HbalancesSerializer
from django.urls import reverse, resolve
from rest_framework import status

class TestAPI(unittest.TestCase):
    def test_balances_api(self):
        headers = {'x-api-key': 'b4a4552e-1eac-44ac-8fcc-91acca085b98-f94b74ce-aa17-48f5-83e2-8b8c30509c18'}
        url = 'https://uh4goxppjc7stkg24d6fdma4t40wxtly.lambda-url.eu-central-1.on.aws/balances'
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)

    def test_transactions_api(self):
        headers = {'x-api-key': 'b4a4552e-1eac-44ac-8fcc-91acca085b98-f94b74ce-aa17-48f5-83e2-8b8c30509c18'}
        url = 'https://uh4goxppjc7stkg24d6fdma4t40wxtly.lambda-url.eu-central-1.on.aws/transactions'
        response = requests.get(url, headers=headers)
        self.assertEqual(response.status_code, 200)

class hbalancesTestCase(TestCase):
    def test_serializer(self):
        data = {"amount": 100,
                "currency": "EUR",
                "date": "2022-06-29",
                "status": "PROCESSED"}
        serializer = HbalancesSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        
    def test_amount_not_given_serializer(self):
        data = {"currency": "EUR",
                "date": "2022-06-29",
                "status": "PROCESSED"}
        serializer = HbalancesSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_currency_not_given_serializer(self):
        data = {"amount": 100,
                "date": "2022-06-29",
                "status": "PROCESSED"}
        serializer = HbalancesSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_date_not_given_serializer(self):
        data = {"amount": 100,
                "currency": "EUR",
                "status": "PROCESSED"}
        serializer = HbalancesSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_status_not_given_serializer(self):
        data = {"amount": 100,
                "currency": "EUR",
                "date": "2022-06-29"}
        serializer = HbalancesSerializer(data=data)
        self.assertTrue(serializer.is_valid())

class HistoricalBalanceListTestCase(TestCase):

    def test_get_historical_balances(self):
        url = reverse('historical-balances-list')

    # def test_get_historical_balances_with_data(self):
    #     url = reverse('historical-balances-list')
    #     response = APIClient.get(url, {'from': '2020-01-01', 'to': '2020-02-02', 'sort': 'desc'})
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     response_data = response.json()
    #     self.assertIsInstance(response_data, list)


class GetTestView(SimpleTestCase):
    def test_balances(self):
        url = reverse("Balances")

    def test_transactions(self):
        url = reverse("Transactions")
from django.shortcuts import render
from rest_framework import generics, permissions, status
from .models import hbalances
from .serializers import HbalancesSerializer
import requests
from django.http import JsonResponse
from datetime import datetime
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
import json 

def Balances(balance):
    headers = {'x-api-key': 'b4a4552e-1eac-44ac-8fcc-91acca085b98-f94b74ce-aa17-48f5-83e2-8b8c30509c18'}
    url = 'https://uh4goxppjc7stkg24d6fdma4t40wxtly.lambda-url.eu-central-1.on.aws/balances'
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

def Transactions(transaction):
    headers = {'x-api-key': 'b4a4552e-1eac-44ac-8fcc-91acca085b98-f94b74ce-aa17-48f5-83e2-8b8c30509c18'}
    url = 'https://uh4goxppjc7stkg24d6fdma4t40wxtly.lambda-url.eu-central-1.on.aws/transactions'
    response = requests.get(url, headers=headers)
    data = response.json()
    return JsonResponse(data)

class HistoricalBalancesList(generics.ListAPIView):
    queryset = hbalances.objects.all()
    serializer_class = HbalancesSerializer
    permission_classes = [permissions.AllowAny]

    def get_queryset(self):
        from_date = self.request.query_params.get('from')
        to_date = self.request.query_params.get('to')
        sort_order = self.request.query_params.get('sort')
        headers = {'x-api-key': 'b4a4552e-1eac-44ac-8fcc-91acca085b98-f94b74ce-aa17-48f5-83e2-8b8c30509c18'}
        balances_url = 'https://uh4goxppjc7stkg24d6fdma4t40wxtly.lambda-url.eu-central-1.on.aws/balances'
        balances_response = requests.get(balances_url, headers=headers)
        balances_data = balances_response.json()
        balances_serializer = HbalancesSerializer(data = balances_data, partial=True)
        transactions_url = 'https://uh4goxppjc7stkg24d6fdma4t40wxtly.lambda-url.eu-central-1.on.aws/transactions'
        transactions_response = requests.get(transactions_url, headers=headers)
        transactions_data = transactions_response.json()
        transactions_serializer = HbalancesSerializer(data = transactions_data, partial=True)
        if balances_serializer.is_valid():
            pass
        else:
            return JsonResponse({"Error": "Balances data is not valid"})
        if transactions_serializer.is_valid():
            pass
        else:
            return JsonResponse({"Error": "Transactions data is not valid"})
        data = []
        data.append({
                    'date': balances_serializer['date'].value,
                    'amount': balances_serializer['amount'].value,
                    'currency': balances_serializer['currency'].value
        })
        previous_amount = balances_serializer['amount'].value
        for transactions in transactions_data.items():
            for transaction in transactions:
                for i in transaction:
                    if type(i)==type({}) and i['status']=='PROCESSED':
                                previous_amount += i['amount']
                                data.append({
                                    'date': i['date'],
                                    'amount': previous_amount,
                                   'currency': i['currency']
                             })
        if sort_order == 'desc':
            data.sort(key=lambda item: item['date'], reverse=True)
        if from_date and to_date: 
            data = [item for item in data if from_date <= item['date'] <= to_date]
        
        return data
from django.test import TestCase
from rest_framework.test import APITestCase
import pytest
from .models import *
from django.urls import reverse
# Create your tests here.


@pytest.mark.django_db
class Loan(APITestCase):
    def test_create_fund_API(self):  
        body = {
        "provider_id": 1,
        "fund": 5000
        }
        url= reverse("create_fund" )
        response= self.client.post(url,body)
        self.assertEqual(response.status_code,200)
        

    def test_create_request_loan_API(self):
        body = {
            "amount": 1000,
            "customer_id": 1,
        }
        url= reverse("request_loan" )
        response= self.client.post(url,body)
        self.assertEqual(response.status_code,200)


    def test_add_fund_API(self):
        body = {
            "fund": 1000,
            "bank":2,
        }
        url= reverse("add_fund" )
        response= self.client.post(url,body)
        self.assertEqual(response.status_code,200)

    
    def test_view_fund_API(self):
        body = {
            "provider_id": 1
        }
        url= reverse("view_fund" )
        response= self.client.post(url,body)
        self.assertEqual(response.status_code,200)


    def test_loan_requests_API(self):
        url= reverse("view_fund" )
        response= self.client.get(url)
        self.assertEqual(response.status_code,200)


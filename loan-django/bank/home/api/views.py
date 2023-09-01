from django.shortcuts import render,redirect
from ..models import loan,loancustomer,loanprovider,bank
from .serializers import *
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate
from django.contrib import messages
from rest_framework.decorators import api_view
from rest_framework.response import Response

# views.py
from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateLoanAPISerializer

def bank_provider(request):                       # render response bank provider template , path for my local machine
    return render(request, '/home/esllam/Desktop/loan-django/bank/templates/bank_provider.html')


# handles user authentication for logging into the system. It checks the provided username and password and redirects the user to the appropriate page based on their role (customer or provider). 
def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        if 'customer' in username:
            auth_login(request, user)
            return redirect('customer')
        elif "provider" in username :
            auth_login(request,user)
            return redirect("provider")
    else:
        messages.error(request,"Invalid username or password.")
    return render(request,'/home/esllam/Desktop/loan-django/bank/templates/login.html',)

#defines an API endpoint for creating a new fund. It receives data from the request, validates it using a serializer, and creates a new bank record with the specified fund amount and provider ID. 
class CreateFund(generics.GenericAPIView):
    def post(self, request):
        serialized_data = AddFundAPISerializer(data=request.data)
        serialized_data.is_valid()
        body = serialized_data.data
        provider_id = body.get('provider_id')
        fund = body.get('fund')
        bank_ = bank(total_budget=fund, provider__id=provider_id)
        bank_.save()
        return Response(
            data={'message':'fund created'}
        )

#handles adding funds to an existing bank record.  retrieves the bank record based on the provided bank ID, and updates the total budget by adding the specified fund amount. 
class AddFund(generics.GenericAPIView):
    def post(self, request):
        serialized_data = AddFundAPISerializer(data=request.data)
        serialized_data.is_valid()
        body = serialized_data.data
        fund = body.get('fund')
        bank_id = body.get('bank')
        bank_ = bank.objects.get(id=bank_id)
        bank_.total_budget = float(bank_.total_budget) + fund
        bank_.save()
        return Response(
            data={'message':'fund added'}
        )
    
    #This class provides an API endpoint to view the fund details for a specific provider. It receives data from the request, validates it using a serializer, retrieves the provider and corresponding bank record, and returns the bank details using a serializer. 
class ViewFund(generics.GenericAPIView):
    def post(self, request):
        serialized_data = ViewFundAPISerializer(data=request.data)
        serialized_data.is_valid()
        body = serialized_data.data
        provider_id = body.get('provider_id')
        provider = loanprovider.objects.filter(id=provider_id).last()
        bank_ = bank.objects.filter(provider=provider).last()
        payload = BankPersonalSerializer(bank_).data
        return Response(
            data=payload
        )
        
    #This class handles creating a new loan request. It receives data from the request, validates it using a serializer, retrieves the customer based on the provided customer ID, and creates a new loan record with the specified loan amount and customer. 
class RequestLoan(generics.GenericAPIView):
    def post(self, request):
        serialized_data = CreateLoanAPISerializer(data=request.data)
        serialized_data.is_valid()
        body = serialized_data.data
        amount = body.get('amount')
        customer_id = body.get('customer')
        customer = loancustomer.objects.get(id=customer_id)
        l = loan(loan_amount=amount, customer=customer)
        l.save()
        return Response(
            data={'message':'loan created successfully'}
        )

#This class provides API endpoints for retrieving and updating loan records. The  get  method retrieves all loans that are not approved yet, while the  post  method receives data from the request, validates it using a serializer, retrieves the loan based on the provided loan ID, and updates the loan details such as duration, bank, interest rate, and approval status. 
class LoansView(generics.GenericAPIView):
    #returns all loans
    def get(self):
        loans = loan.objects.filter(approved=False)
        payload = LoanSerializer(loans, many=True).data
        return Response(
            data=payload
        )

#specific loanID with the duration , bank, interest rate will approve the loan
    def post(self, request):
        serialized_data = CreateLoanAPISerializer(data=request.data)
        serialized_data.is_valid()
        body = serialized_data.data
        loan_id = body.get('loan_id')
        duration = body.get('duration')
        bank = body.get('bank')
        interest_rate = body.get('interest_rate')
        loan_ = loan.objects.get(id=loan_id)
        loan_.duration = duration
        loan_.bank = bank
        loan_.interest_rate = interest_rate
        loan_.approved = True
        loan_.save()
        return Response(
            data={'message': 'approved successfully'}
        )

    
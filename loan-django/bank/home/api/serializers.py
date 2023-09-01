from rest_framework import serializers
from django.contrib.auth.models import User
from ..models import loan,loancustomer,loanprovider,bank


class LoanProviderSerializer(serializers.ModelSerializer):
    class Meta:
        model = loanprovider
        fields = ['id','name','mobile','email','password','provide_history']

class LoanCustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = loancustomer
        fields = '__all__'

class BankPersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = bank
        fields = '__all__'

class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model = loan
        fields = '__all__'

class CreateLoanAPISerializer(serializers.Serializer):
    amount = serializers.FloatField()
    duration = serializers.IntegerField()
    interest_rate = serializers.FloatField()
    minimum_salary = serializers.FloatField()
    bank = serializers.IntegerField()
    customer = serializers.IntegerField()

class AddFundAPISerializer(serializers.Serializer):
    provider_id = serializers.IntegerField()
    fund = serializers.FloatField()
    bank = serializers.IntegerField()

class ViewFundAPISerializer(serializers.Serializer):
    provider_id = serializers.IntegerField()

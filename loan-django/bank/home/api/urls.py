from django.urls import path, include
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()


urlpatterns = [
    path('', views.login,name='login'),
    path('customer/request_loan/', views.RequestLoan.as_view()),   # handle customer request loan with specific amount from bank (takes customerID , amount )
    path('provider/add_fund/', views.AddFund.as_view()),           # handle provider to addfund with specific amount
    path('provider/create_fund/', views.CreateFund.as_view()),     # handle request for provider to create new fund 
    path('provider/view_fund/', views.ViewFund.as_view()),         # request to view the details of a specific fund 
    path('banker/loan_requests/', views.LoansView.as_view()),       # view all the loans requests made by customer

]


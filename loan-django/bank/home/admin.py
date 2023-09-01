from django.contrib import admin
from .models import loan,loancustomer,loanprovider,bank
# Register your models here.
admin.site.register(loan)
admin.site.register(loancustomer)
admin.site.register(loanprovider)
admin.site.register(bank)
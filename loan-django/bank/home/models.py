from django.db import models
# venv\Scripts\activate
# Create your models here.

DURATION_CHOICES = (
    ('6month','6 MONTHS'),
    ('12month', '12 MMONTHS'),
    ('18month','18 MONTHS'),
    ('24month','24 MONTHS'),
    ('36month','36 MONTHS'),
)

class loanprovider(models.Model):
    name = models.CharField(max_length=200)
    mobile=models.IntegerField(max_length=11)
    email=models.CharField(max_length=50,null=False)
    password=models.CharField(max_length=50,null=False)
    

class loancustomer(models.Model):
    name = models.CharField(max_length=200)
    mobile=models.IntegerField(max_length=11)
    email=models.CharField(max_length=50,null=False)
    password=models.CharField(max_length=50,null=False)
    salary=models.DecimalField(max_digits=10, decimal_places=2)

class bank(models.Model):
    total_budget=models.DecimalField(max_digits=10, decimal_places=2)
    provider=models.ForeignKey(loanprovider, on_delete=models.CASCADE)


class loan(models.Model):
    loan_amount=models.DecimalField(max_digits=10, decimal_places=2)
    duration=models.CharField(max_length=7, choices=DURATION_CHOICES, default='6month', null=True)
    interest_rate= models.DecimalField(max_digits=5, decimal_places=2, null=True)
    bank = models.ForeignKey(bank, on_delete=models.CASCADE, null=True)
    customer = models.ForeignKey(loancustomer, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)
    @property
    def interest_price(self):
        if self.duration=='6month':
            return self.interest_rate==0.05
        elif self.duration=='12month':
            return self.interest_rate==0.1   
        elif self.duration=='18month':
            return self.interest_rate==0.15
        elif self.duration=='24month':
            return self.interest_rate==0.18
        elif self.duration=='36month':
            return self.interest_rate==0.2
    @property
    def total_price(self):
        self.total_loan=self.loan_amount +(self.loan_amount * self.interest_rate)        
        return self.total_loan




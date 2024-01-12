from django.db import models
from django.contrib.auth.models import User
class UserAccount(models.Model):
    user=models.OneToOneField(User,related_name='account',on_delete=models.CASCADE)
    account_no=models.IntegerField(unique=True)
    balance=models.DecimalField(default=0,decimal_places=2,max_digits=10)
    initial_deposit_date = models.DateField(auto_now_add=True)

    def __str__(self):
            return str(self.account_no)
    
class Deposit(models.Model):
    account=models.ForeignKey(UserAccount,related_name="deposit",on_delete=models.CASCADE)
    amount=models.DecimalField(decimal_places=2,max_digits=10)
    timestamp=models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return str(self.account.account_no)
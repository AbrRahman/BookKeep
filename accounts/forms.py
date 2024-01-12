from collections.abc import Mapping
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from accounts.models import UserAccount,Deposit
class UserAccountForm(UserCreationForm):
    class Meta:
        model=User
        fields=['username','first_name','last_name','email','password1','password2']

    def save(self, commit: True):
        our_user= super().save(commit=False)
        if commit:
            our_user.save()
            UserAccount.objects.create(
                user=our_user,
                account_no=100+our_user.id
            )

        return our_user

    
class DepositForm(forms.ModelForm):
    class Meta:
        model=Deposit
        fields=['amount']
    
    def __init__(self,*args, **kwargs):
        self.account = kwargs.pop('account')
        super().__init__(*args, **kwargs)
    def save(self,commit=True):
        self.instance.account=self.account
        return super().save()

    def clean_amount(self):
        amount=self.cleaned_data.get('amount')
        if amount<100:
            raise ValidationError('Deposit must be gether then 100 tk')
        return amount
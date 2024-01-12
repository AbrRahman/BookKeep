from django.contrib import admin
from accounts.models import UserAccount,Deposit
admin.site.register(UserAccount)
admin.site.register(Deposit)
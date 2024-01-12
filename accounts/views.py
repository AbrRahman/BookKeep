from django.shortcuts import render,redirect
from django.views.generic import FormView,CreateView
from django.contrib.auth.views import LoginView
from accounts.forms import UserAccountForm,DepositForm
from django.urls import reverse_lazy
from django.contrib.auth import login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from books.models import Borrow
from django.contrib.auth.decorators import login_required
from django.contrib import messages
class UserRegisterView(FormView):
    form_class=UserAccountForm
    template_name="accounts/user_register.html"
    success_url = reverse_lazy("register")

    def form_valid(self, form):
        form.save(commit=True)
        messages.success(self.request,"Registration Success")
        # login(self.request,user)
        return super().form_valid(form)
    
class UserLoginView(LoginView):
    template_name='accounts/login.html'
    def get_success_url(self):
        messages.success(self.request,"Login Successfully")
        return reverse_lazy('profile')

class DepositMoneyView(LoginRequiredMixin,CreateView):
    form_class=DepositForm
    template_name='accounts/deposit_money.html'
    success_url = reverse_lazy('register')

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({"account": self.request.user.account})
        return kwargs

    def form_valid(self, form):
        amount=form.cleaned_data.get('amount')
        account = self.request.user.account
        account.balance+=amount
        account.save(
            update_fields=[
                'balance'
            ]
        )
        messages.success(self.request,f"Successfully {amount} tk deposit")
        return super().form_valid(form)
    
    
@login_required
def userLogout(request):
    logout(request)
    messages.success(request,"Successfully Logout")
    return redirect('home')

@login_required
def profile(request):
    account=request.user.account
    borrow=Borrow.objects.filter(account=account)
    return render(request,"accounts/profile.html",{"borrow":borrow})
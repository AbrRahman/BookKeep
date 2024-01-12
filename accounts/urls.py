from django.urls import path
from .views import UserRegisterView,UserLoginView,userLogout,profile,DepositMoneyView
urlpatterns = [
    path('register/', UserRegisterView.as_view(),name='register'),
    path('login/', UserLoginView.as_view(),name='login'),
    path('logout/', userLogout,name='logout'),
    path('deposit/', DepositMoneyView.as_view(),name='deposit'),
    path('profile/', profile,name='profile'),

]

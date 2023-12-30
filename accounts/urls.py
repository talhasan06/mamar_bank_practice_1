
from django.urls import path
from .views import UserRegistrationFormView,UserLoginView,UserLogoutView,UserBankAccountUpdateView,TransferBalanceView
urlpatterns = [
    path('register/',UserRegistrationFormView.as_view(),name='register'),
    path('login/',UserLoginView.as_view(),name='login'),
    path('logout/',UserLogoutView.as_view(),name='logout'),
    path('profile/', UserBankAccountUpdateView.as_view(), name='profile' ),
    path('transfer_balance/', TransferBalanceView.as_view(), name='transfer_balance' ),
]

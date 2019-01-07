from django.urls import path

from products.views import UserProductHistoryView
from .views import AccountHomeView, AccountEmailActivationView, UserDetailUpdateView


urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
    path('details/', UserDetailUpdateView.as_view(), name='user-update'),
    path('history/products/', UserProductHistoryView.as_view(), name='user-product-history'),
    path('email/confirm/<key>/', AccountEmailActivationView.as_view(), name='email-activate'),
    path('email/resend-activation/', AccountEmailActivationView.as_view(), name='resend-activation'),
]

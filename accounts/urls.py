from django.urls import path

from .views import AccountHomeView, AccountEmailActivationView, UserDetailUpdateView


urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
    path('details/', UserDetailUpdateView.as_view(), name='user-update'),
    path('email/confirm/<key>/', AccountEmailActivationView.as_view(), name='email-activate'),
    path('email/resend-activation/', AccountEmailActivationView.as_view(), name='resend-activation'),
]

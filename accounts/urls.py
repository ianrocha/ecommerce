from django.urls import path

from .views import AccountHomeView, AccountEmailActivationView


urlpatterns = [
    path('', AccountHomeView.as_view(), name='home'),
    path('email/confirm/<key>/', AccountEmailActivationView.as_view(), name='email-activate'),
    path('email/resend-activation/', AccountEmailActivationView.as_view(), name='resend-activation'),
]

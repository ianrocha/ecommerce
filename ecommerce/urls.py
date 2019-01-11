"""ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static

from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView, RedirectView
from django.contrib.auth.views import LogoutView

from accounts.views import LoginView, RegisterView, GuestRegisterView
from addresses.views import (AddressCreateView,
                             AddressListView,
                             AddressUpdateView,
                             checkout_address_create_view,
                             checkout_address_reuse_view)
from billing.views import payment_method_view, payment_method_create_view
from carts.views import cart_detail_api_view
from marketing.views import MarketingPreferenceUpdateView, MailchimpWebHookView
from orders.views import LibraryView
from . import views


urlpatterns = [
    path('', views.home_page, name='home'),
    path('admin/', admin.site.urls),
    # path('about/', views.about_page, name='about'),
    # path('contact/', views.contact_page, name='contact'),
    path('accounts/', RedirectView.as_view(url='/account')),
    path('account/', include(('accounts.urls', 'account'), namespace='account')),
    path('accounts/', include('accounts.passwords.urls')),
    path('address/', RedirectView.as_view(url='/addresses')),
    path('addresses/', AddressListView.as_view(), name='addresses'),
    path('addresses/create/', AddressCreateView.as_view(), name='address-create'),
    path('addresses/<pk>/', AddressUpdateView.as_view(), name='address-update'),
    path('login/', LoginView.as_view(), name='login'),
    path('checkout/address/create/', checkout_address_create_view, name='checkout_address_create'),
    path('checkout/address/reuse/', checkout_address_reuse_view, name='checkout_address_reuse'),
    path('register/guest/', GuestRegisterView.as_view(), name='guest_register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('api/cart/', cart_detail_api_view, name='api-cart'),
    path('cart/', include(('carts.urls', 'cart'), namespace='cart')),
    path('billing/payment-method/', payment_method_view, name='billing-payment-method'),
    path('billing/payment-method/create/', payment_method_create_view, name='billing-payment-method-endpoint'),
    path('register/', RegisterView.as_view(), name='register'),
    path('library/', LibraryView.as_view(), name='library'),
    path('orders/', include(('orders.urls', 'orders'), namespace='orders')),
    path('products/', include(('products.urls', 'products'), namespace='products')),
    path('search/', include(('search.urls', 'search'), namespace='search')),
    path('settings/', RedirectView.as_view(url='/account')),
    path('settings/email/', MarketingPreferenceUpdateView.as_view(), name='marketing-pref'),
    path('webhooks/mailchimp/', MailchimpWebHookView.as_view(), name='webhooks-mailchimp'),
    path('bootstrap/', TemplateView.as_view(template_name='bootstrap/example.html')),
]

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

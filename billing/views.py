from django.shortcuts import render

import stripe
stripe.api_key = 'sk_test_WNgx9dyqpq0F7ybQ7LAVOqzZ'
STRIPE_PUB_KEY = 'pk_test_vX0k7ckAxcB3vBAqygOXGKLt'


def payment_method_view(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'billing/payment-method.html', {'publish_key': STRIPE_PUB_KEY})

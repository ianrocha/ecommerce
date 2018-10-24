from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.utils.http import is_safe_url

import stripe
stripe.api_key = 'sk_test_WNgx9dyqpq0F7ybQ7LAVOqzZ'
STRIPE_PUB_KEY = 'pk_test_vX0k7ckAxcB3vBAqygOXGKLt'


def payment_method_view(request):
    next_url = None
    next_ = request.GET.get('next')
    print(next_)
    if is_safe_url(next_, request.get_host()):
            next_url = next_
    return render(request, 'billing/payment-method.html', {'publish_key': STRIPE_PUB_KEY, 'next_url': next_url})


def payment_method_create_view(request):
    if request.method == 'POST':
        print(request.POST)
        return JsonResponse({'message': 'Success! Your card was added.'})
    return HttpResponse('error', status=401)

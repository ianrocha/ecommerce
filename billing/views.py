from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils.http import is_safe_url

import stripe

from .models import BillingProfile, Card

stripe.api_key = 'sk_test_WNgx9dyqpq0F7ybQ7LAVOqzZ'
STRIPE_PUB_KEY = 'pk_test_vX0k7ckAxcB3vBAqygOXGKLt'


def payment_method_view(request):
    # if request.user.is_authenticated:
    #     billing_profile = request.user.billingprofile
    #     my_customer_id = billing_profile.customer_id
    billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
    if not billing_profile:
        return redirect("/cart")

    next_url = None
    next_ = request.GET.get('next')
    if is_safe_url(next_, request.get_host()):
            next_url = next_
    return render(request, 'billing/payment-method.html', {'publish_key': STRIPE_PUB_KEY, 'next_url': next_url})


def payment_method_create_view(request):
    if request.method == 'POST':
        billing_profile, billing_profile_created = BillingProfile.objects.new_or_get(request)
        if not billing_profile:
            return HttpResponse({"message": "Cannot find this user"}, status=401)

        token = request.POST.get("token")
        if token is not None:
            # customer = stripe.Customer.retrieve(billing_profile.customer_id)
            # card_response = customer.sources.create(source=token)
            # new_card_obj = Card.objects.add_new(billing_profile=billing_profile, stripe_card_response=card_response)
            new_card_obj = Card.objects.add_new(billing_profile, token)
            print(new_card_obj)  # start saving our cards too
            return JsonResponse({'message': 'Success! Your card was added.'})

    return HttpResponse('error', status=401)

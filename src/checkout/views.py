# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.conf import settings
from profiles.models import profile,userStripe,order
# Create your views here.
import stripe
stripe.api_key = "sk_test_KGb17EJmeW1nyHnkCkAVcHCI"

# Create your views here.


@login_required
def checkout(request,total='1'):
    customer_id = request.user.userstripe.stripe_id
    total = total
    user = profile.objects.get(user=request.user)
    order.objects.filter(client=user).delete()
    if request.method == 'POST':
        token = request.POST['stripeToken']
        try:
            total = total*100
            customer = stripe.Customer.retrieve(customer_id)
            customer.sources.create(source=token)
            charge  = stripe.Charge.create(
            amount      = total,
            currency    = "usd",
            customer    = customer,
            description = "The product charged to the user"
            )
        except stripe.error.CardError as ce:
            return False, ce
    context = { "stripe_key": settings.STRIPE_PUBLIC_KEY }
    template = 'checkout.html'
    return render(request,template,context)

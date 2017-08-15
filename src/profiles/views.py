# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import profile,userStripe,order
# Create your views here.

listDict = [
{'name': 'SRS',
'price': 20,
'id': '1'},
{'name':'qqq',
'price': 40,
'id':'2'},
{'name':'xxx',
'price': 40,
'id':'3'},
{'name': 'werr',
'price': 50,
'id':'4'}
]

def home(request):
    localDic = listDict
    print localDic
    context = locals()
    template = 'home.html'
    return render(request,template,context,{'localDic':localDic})

def about(request):
    context = locals()
    template = 'about.html'
    return render(request,template,context)

@login_required
def userProfile(request):
    user = request.user
    context = {'user': user}
    template = 'profile.html'
    return render(request,template,context)

def history(request):
    context = locals()
    template = 'history.html'
    return render(request,template,context)


@login_required
def cart(request,item='1'):
    user = profile.objects.get(user=request.user)
    if request.method == 'POST':
        id = request.POST['element.item_id']
        order.objects.filter(item_id = id, client=user).delete()
    total =0
    cartItems = []
    for element in listDict:
        if element['id'] == item:
            cartItems.append(element)
            o1 = order.objects.create(item_name=element['name'],item_price=element['price'], item_id=element['id'],client=user)
            o1.save()
    for ele in order.objects.filter(client=user):
        cartItems.append(ele)
        total = total + ele.item_price
    #print total
    context = {'cartItems': cartItems, 'total': total}
    template = 'cart.html'
    return render(request,template,context)

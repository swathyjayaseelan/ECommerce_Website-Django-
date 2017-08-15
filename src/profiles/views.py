# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import profile,userStripe,order
# Create your views here.

listDict = [
{'name': 'Software Requirements',
'price': 20,
'isbn': '1234',
'img': 'softwarereq.jpg',
'id': '1'},
{'name':'Python: The Complete Reference by Martin C Brown',
'price': 40,
'isbn': '9780072127188',
'img':  'python.jpg',
'id':'2'},
{'name':'Pro JavaScript Techniques by John Resig',
'price': 11,
'img': 'javascript.gif',
'isbn': ' 978-1590597279',
'id':'3'},
{'name': 'Python Machine Learning',
'price': 30,
'isbn': '1783555130',
'img': 'machine.png',
'id':'4'},
{'name': 'ReactJS',
'price': 39,
'isbn': '1783555130',
'img': 'react.png',
'id':'4'},
{'name': 'Full Stack Development with MEAN',
'price': 50,
'isbn': '1783555130',
'img': 'mean.jpg',
'id':'4'},
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
        deleteid = request.POST['element.id']
        order.objects.filter(id = deleteid, client=user).delete()
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

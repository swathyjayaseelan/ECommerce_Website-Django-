# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import contactForm
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.
def contact(request):
    title = 'Contact'
    form = contactForm(request.POST or None)
    context = {'title':title, 'form':form}
    if form.is_valid():
        print form.cleaned_data['email']
        name = form.cleaned_data['name']
        comment = form.cleaned_data['comment']
        subject = 'Message from mysite.com'
        message = '%s %s' %(comment,name)
        emailFrom = form.cleaned_data['email']
        emailTo = [settings.EMAIL_HOST_USER]
        send_mail(subject,message,emailFrom,emailTo,fail_silently=True)
        title = 'Thanks!'
        confirm_message = 'We will get back to you!'
        context = {'title':title, 'confirm_message':confirm_message,}
    template = 'contact.html'
    return render(request,template,context)

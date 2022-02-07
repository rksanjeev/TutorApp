from django import forms
from django.forms import ModelForm
from . import models


class ContactForm(ModelForm):
    class Meta:
        model = models.LeadModel
        fields = ('name', 'email', 'subject', 'message', 'phone')


class loginForm(ModelForm):
    class Meta:
        model = models.LeadModel
        fields = ('name', 'email', 'subject', 'message', 'phone')



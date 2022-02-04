from re import template
from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from . import forms
# Create your views here.

class IndexPage(TemplateView):
    template_name = 'home.html'

class AboutPage(TemplateView):
    template_name = 'about.html'    

class ContactPage(FormView):
    template_name = 'contact.html'
    form_class = forms.ContactForm
    

class PrivacyPage(TemplateView):
    template_name = 'privacy.html'
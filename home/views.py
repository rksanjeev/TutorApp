from re import template
from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class IndexPage(TemplateView):
    template_name = 'home.html'

class AboutPage(TemplateView):
    template_name = 'about.html'    

class ContactPage(TemplateView):
    template_name = 'contact.html'

class PrivacyPage(TemplateView):
    template_name = 'privacy.html'
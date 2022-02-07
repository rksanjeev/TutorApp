from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.contrib import messages
from . import forms
# Create your views here.

class IndexPage(TemplateView):
    template_name = 'home.html'

class AboutPage(TemplateView):
    template_name = 'about.html'  
    
      
class tutoringservicesPage(TemplateView):
    template_name = 'tutoringservices.html' 

class ExamPreprationServicesPage(TemplateView):
    template_name = 'ExamPreprationServices.html' 


class CollegeAdmissionsGuidancePage(TemplateView):
    template_name = 'CollegeAdmissionsGuidance.html' 



   


class ContactPage(FormView):
    template_name = 'contact.html'
    form_class = forms.ContactForm
    success_url = '/contact'

    def form_valid(self, form):
        messages.success(self.request, 'Contact request submitted successfully.')
        form.save()
        return redirect(self.success_url )
    

class PrivacyPage(TemplateView):
    template_name = 'privacy.html'
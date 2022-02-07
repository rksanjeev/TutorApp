from django.urls import path, include
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index' ),
    path('about/', views.AboutPage.as_view(), name='about'),
    path('tutoringservices/', views.tutoringservicesPage.as_view(), name='tutoringservices'),
    path('ExamPreprationServices/', views.ExamPreprationServicesPage.as_view(), name='ExamPreprationServices'),
    path('CollegeAdmissionsGuidance/', views.CollegeAdmissionsGuidancePage.as_view(), name='CollegeAdmissionsGuidance'),
    path('contact/', views.ContactPage.as_view(), name='contact'),
    path('privacy-policy/', views.PrivacyPage.as_view(), name='privacy'),
]

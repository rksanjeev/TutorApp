from django.urls import path, include
from . import views
app_name = 'home'

urlpatterns = [
    path('', views.IndexPage.as_view(), name='index' ),
    path('/about', views.AboutPage.as_view(), name='about'),
    path('/contact', views.ContactPage.as_view(), name='contact'),
    path('/privacy-policy', views.PrivacyPage.as_view(), name='privacy'),
]


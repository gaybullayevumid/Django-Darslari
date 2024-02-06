from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'pages/home.html'

class ServisePageView(TemplateView):
    template_name = 'pages/service.html'

class ProjectPageView(TemplateView):
    template_name = 'pages/project.html'

class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'
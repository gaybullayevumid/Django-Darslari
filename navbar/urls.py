from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('service/', ServisePageView.as_view(), name='service'),
    path('project/', ProjectPageView.as_view(), name='project'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]

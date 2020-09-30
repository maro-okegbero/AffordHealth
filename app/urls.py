from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
                path('about', AboutView.as_view(), name='about'),
                path('contact', ContactView.as_view(), name='contact'),
                path('', ContactView.as_view(), name='homepage')
]

from django.contrib import admin
from django.urls import path, include
from app.views import *

urlpatterns = [
                path('', HomepageView.as_view(), name='homepage'),
                path('about', AboutView.as_view(), name='about'),
                path('contact', ContactView.as_view(), name='contact'),
                path('blog', BlogListView.as_view(), name='blog'),
                path('blog/<pk>', BlogDetailView.as_view(), name='blog_detail'),
                path('causes', CausesList.as_view(), name='causes'),
                path('causes/<pk>', CausesDetail.as_view(), name='cause_detail'),
                path('faq', FaqView.as_view(), name='faq'),
                path('login', LoginView.as_view(), name='login'),
                path('signup', RegisterView.as_view(), name='signup'),
]

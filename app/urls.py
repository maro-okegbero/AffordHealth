from django.contrib import admin
from django.urls import path, include
from app.views import *


urlpatterns = [
                path('', HomepageView.as_view(), name='homepage'),
                path('about', AboutView.as_view(), name='about'),
                path('contact', ContactView.as_view(), name='contact'),
                path('blog', BlogListView.as_view(), name='blog'),
                path('blog/<pk>', BlogDetailView.as_view(), name='blog_detail'),
                path('cases', CasesList.as_view(), name='cases'),
                path('personal_cases', PersonalCasesList.as_view(), name='personal_cases'),
                path('cases/submit', CaseCreate.as_view(), name='submit_case'),
                path('cases/<pk>', CasesDetail.as_view(), name='case_detail'),
                path('faq', FaqView.as_view(), name='faq'),
                path('privacy_policy', PrivacyPolicyView.as_view(), name='policy'),
                path('login', LoginView.as_view(), name='login'),
                path('signup', RegisterView.as_view(), name='signup'),
                path('team', Team.as_view(), name='team'),
                path('comment', comment_ajax, name='comment'),

]

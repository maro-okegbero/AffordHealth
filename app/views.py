from django.shortcuts import render
from django.views.generic.base import TemplateView
from app.models import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy

from accounts.forms import LoginForm, RegisterForm


class AboutView(TemplateView):
    template_name = "app/about.html"


class BlogListView(ListView):
    template_name = 'app/blog-1.html'
    model = BlogPost
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'app/single-blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CausesList(ListView):
    template_name = 'app/causes.html'
    model = Cause
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class CausesDetail(DetailView):
    model = BlogPost
    template_name = 'app/single-causes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context


class ContactView(TemplateView):
    template_name = "app/contact.html"


class FaqView(TemplateView):
    template_name = "app/faq.html"


class HomepageView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['causes'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'app/log-in.html'


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'app/sign-up.html'
    success_url = reverse_lazy('login')


class Team(TemplateView):
    template_name = "app/team.html"


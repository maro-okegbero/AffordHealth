from django.views.generic import CreateView, FormView
from django.views.generic.base import TemplateView
from django.db.models import Q
from app.forms import CausesForm
from app.models import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from accounts.forms import LoginForm, RegisterForm


class AboutView(TemplateView):
    template_name = "app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class BlogListView(ListView):
    template_name = 'app/blog-1.html'
    model = BlogPost
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class BlogDetailView(DetailView):
    model = BlogPost
    template_name = 'app/single-blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context_object = context['object']
        object_title = context_object.title
        context['blog_posts'] = BlogPost.objects.exclude(title__exact=object_title)[:3]
        return context


class CasesList(ListView):
    template_name = 'app/causes.html'
    model = Cause
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class CasesDetail(DetailView):
    model = Cause
    template_name = 'app/single-causes.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context_object = context['object']
        object_description = context_object.description
        context['cases'] = Cause.objects.exclude(description__exact=object_description)[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class CaseCreate(FormView):
    template_name = 'app/causes_form.html'
    form_class = CausesForm
    success_url = '/cases'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.
        form.send_email()
        form.user = self.request.user
        form.save()
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class ContactView(TemplateView):
    template_name = "app/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class FaqView(TemplateView):
    template_name = "app/faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class HomepageView(TemplateView):
    template_name = 'app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class LoginView(auth_views.LoginView):
    form_class = LoginForm
    template_name = 'app/log-in.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class RegisterView(generic.CreateView):
    form_class = RegisterForm
    template_name = 'app/sign-up.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


class Team(TemplateView):
    template_name = "app/team.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context

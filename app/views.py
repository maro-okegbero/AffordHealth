from django import forms
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView, View
from django.views import View
from django.db.models import Q
from app.forms import CausesForm
from app.models import *
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.contrib.auth import views as auth_views, authenticate, login, logout
from django.views import generic
from django.urls import reverse_lazy
from accounts.forms import LoginForm, BootstrapModelForm, RegisterForm


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
        try:
            approved = Cause.objects.filter(approved=True)
        except Exception as e:
            approved = []

        context['page_obj'] = approved
        print(approved)

        return context


@method_decorator(login_required, name='dispatch')
class PersonalCasesList(ListView):
    template_name = 'app/personal_causes.html'
    model = Cause
    paginate_by = 6

    def get_context_data(self, **kwargs):
        user = self.request.user
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['blog_posts'] = BlogPost.objects.all()[:3]

        try:
            approved = Cause.objects.filter(user=user, approved=True)
        except Exception as e:
            approved = []

        try:
            unapproved = Cause.objects.get(user=user, approved=True)
        except Exception as e:
            unapproved = []

        context['approved'] = approved
        context['unapproved'] = unapproved
        print(user)
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


@method_decorator(login_required, name='dispatch')
class CaseCreate(FormView):
    template_name = 'app/causes_form.html'
    form_class = CausesForm
    success_url = '/cases'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
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


class PrivacyPolicyView(TemplateView):
    template_name = "app/privacy-policy.html"

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


class LoginView(View):
    form_class = LoginForm
    template_name = 'app/log-in.html'
    success_url = reverse_lazy('personal_cases')

    def get(self, request, *args, **kwargs):
        context = dict()
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        context['form'] = self.form_class()
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = dict()
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        context['form'] = form
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            merchant = authenticate(username=username, password=raw_password)
            if merchant:
                login(request, merchant)
                return HttpResponseRedirect('/personal_cases')
            else:
                context['errors'] = "The username or password is wrong"
                logout(request)
                return render(request, self.template_name, context)

        return render(request, self.template_name,context)


class RegisterView(View):
    form_class = RegisterForm
    template_name = 'app/sign-up.html'
    success_url = reverse_lazy('personal_cases')

    def get(self, request, *args, **kwargs):
        context = dict()
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        form = self.form_class()
        context['form'] = form
        print(context, "context..........")
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            merchant = authenticate(username=username, password=raw_password)
            login(request, merchant)

            return HttpResponseRedirect('/personal_cases')

        return render(request, self.template_name, {'form': form})


class Team(TemplateView):
    template_name = "app/team.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return context


def comment_ajax(request):
    """
    comment on a blogpost
    :param request:
    :return:
    """
    if request.is_ajax:
        print("HELlo========================================")
        name = request.GET.get("name")
        body = request.GET.get("body")
        email = request.GET.get("email")
        blog_id = request.GET.get("blog_id")
        data = {}

        if name and body and email and blog_id:
            print("YESSSSSSSS========================================")
            try:
                blog = BlogPost.objects.get(pk=blog_id)
                comment = Comment.objects.create(name=name, body=body, email=email, blog=blog)
                data = {"success": True, "message": "comment was created successfully"}
            except (BlogPost.DoesNotExist, Exception) as e:
                data = {"success": False, "message": e}

            return JsonResponse(data)
        print("Nooooooooooooooooooooooooooo=--=====================")

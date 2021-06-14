import json

from django import forms
from django.contrib.auth.decorators import login_required
from django.forms import modelform_factory
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import TemplateView
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
import requests as reqii
from Afford_Health.settings import PAYSTACK_VERIFY_TRANSACTION_URL, PAYSTACK_SECRET_KEY


class AboutView(TemplateView):
    template_name = "app/about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        context['about_nav'] = "active"
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = ""
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = ""

        return context


class BlogListView(ListView):
    template_name = 'app/blog-1.html'
    model = BlogPost
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['blog_posts'] = BlogPost.objects.all()[:3]
        context['about_nav'] = ""
        context['blog_nav'] = "active"
        context['home_nav'] = ""
        context['cases_nav'] = ""
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = ""
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
        context['about_nav'] = ""
        context['blog_nav'] = "active"
        context['home_nav'] = ""
        context['cases_nav'] = ""
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = ""
        return context


class CasesList(ListView):
    template_name = 'app/causes.html'
    model = Cause
    paginate_by = 6

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['blog_posts'] = BlogPost.objects.all()[:3]
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = "active"
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = ""
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
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = "active"
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = ""

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


class CasesDetail(View):
    model = Cause
    template_name = 'app/single-causes.html'

    def get(self, request, pk, *args, **kwargs):
        context = dict()
        print(args, "hello this args=====")
        context['now'] = timezone.now()
        context['object'] = Cause.objects.get(pk=pk)
        context_object = context['object']
        object_description = context_object.description
        context['cases'] = Cause.objects.exclude(description__exact=object_description)[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = "active"
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = ""
        return render(request, self.template_name, context)

    def post(self, request, pk, *args, **kwargs):
        context = dict()
        print(args, "hello this args=====")
        context['now'] = timezone.now()
        context['object'] = Cause.objects.get(pk=pk)
        context_object = context['object']
        object_description = context_object.description
        context['cases'] = Cause.objects.exclude(description__exact=object_description)[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = "active"
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = ""
        return render(request, self.template_name, context)


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
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = "active"
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = ""
        return context


class ContactView(TemplateView):
    template_name = "app/contact.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = ""
        context['user_nav'] = ""
        context['contact_nav'] = "active"
        context['team_nav'] = ""
        return context


class DonateGenerally(View):
    template_name = "app/donate.html"

    def get(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        context = dict()
        context['cases'] = Cause.objects.all()[:5]
        context['reference'] = "general_payment" + str(random.randint(1, 10000))
        context['blog_posts'] = BlogPost.objects.all()[:3]
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        """

        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        return render(request, self.template_name, context=dict())


class FaqView(TemplateView):
    template_name = "app/faq.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = ""
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = ""
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
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = "active"
        context['cases_nav'] = ""
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = ""
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
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = ""
        context['user_nav'] = "active"
        context['contact_nav'] = ""
        context['team_nav'] = ""
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        context = dict()
        context['cases'] = Cause.objects.all()[:5]
        context['blog_posts'] = BlogPost.objects.all()[:3]
        context['form'] = form
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = ""
        context['user_nav'] = "active"
        context['contact_nav'] = ""
        context['team_nav'] = ""
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

        return render(request, self.template_name, context)


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
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = ""
        context['user_nav'] = "active"
        context['contact_nav'] = ""
        context['team_nav'] = ""
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
        context['about_nav'] = ""
        context['blog_nav'] = ""
        context['home_nav'] = ""
        context['cases_nav'] = ""
        context['user_nav'] = ""
        context['contact_nav'] = ""
        context['team_nav'] = "active"
        return context


def verify_donation(request):
    """
    verify that a donation is legitimate
    :param request:
    :return:
    """
    reference_code = request.POST.get("reference_code")
    url = PAYSTACK_VERIFY_TRANSACTION_URL + reference_code
    headers = {"Authorization": PAYSTACK_SECRET_KEY}
    req = reqii.get(url=url, headers=headers)
    print("I hit here before the request place-----------------")
    print(req.status_code, "This is the status code----------------------------------------------------------")
    print(reference_code, "The reference code==============================")
    if req.status_code == "200":
        print("I am verifying things on the backend halleluya! ")
        response = req.json()
        status = response.get('data').get('status')
        amount = response.get('data').get('amount')
        donor_name = response.get('data').get('authorization').get("account_name")
        if status == "successful":
            cause = Cause.objects.get(reference_code=reference_code)
            cause.donor_count += 1
            cause.donated = amount
            cause.save()
            DonationTransactionHistory(cause=cause, donor_name=donor_name, amount_donated=amount).save()
            return HttpResponse(
                json.dumps({"nothing to see": "this isn't happening"}),
                content_type="application/json"
            )
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )
    return HttpResponse(
        json.dumps({"nothing to see": "this isn't happening"}),
        content_type="application/json"
    )

# def comment_ajax(request):
#     """
#     comment on a blogpost
#     :param request:
#     :return:
#     """
#     if request.is_ajax:
#         print("HELlo========================================")
#         name = request.GET.get("name")
#         body = request.GET.get("body")
#         email = request.GET.get("email")
#         blog_id = request.GET.get("blog_id")
#         data = {}
#
#         if name and body and email and blog_id:
#             print("YESSSSSSSS========================================")
#             try:
#                 blog = BlogPost.objects.get(pk=blog_id)
#                 comment = Comment.objects.create(name=name, body=body, email=email, blog=blog)
#                 data = {"success": True, "message": "comment was created successfully"}
#             except (BlogPost.DoesNotExist, Exception) as e:
#                 data = {"success": False, "message": e}
#
#             return JsonResponse(data)
#         print("Nooooooooooooooooooooooooooo=--=====================")

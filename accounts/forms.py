from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import get_user_model, authenticate, login
from django import forms
from django.forms import ModelForm


class BootstrapModelForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(BootstrapModelForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control'
            })


class RegisterForm(UserCreationForm):
    email = forms.EmailField(max_length=254, required=True, label="Email",
                             widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email"}))

    username = forms.CharField(max_length=30, required=True, label="Username",
                               widget=forms.TextInput(attrs={'class': 'form-control',
                                                             'placeholder': 'Username', }))
    password1 = forms.CharField(max_length=30, required=True, label="Username",
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Type Password', }))
    password2 = forms.CharField(max_length=30, required=True, label="Username",
                                widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                  'placeholder': 'Type Password again', }))

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')


class LoginForm(forms.Form):
    username = forms.CharField(label='Email / Username', widget=forms.TextInput(attrs={'class': 'form-control',
                                                                                       'placeholder': 'Username', }))
    password = forms.CharField(label='password', widget=forms.PasswordInput(attrs={'class': 'form-control',
                                                                                   'placeholder': 'Password', }))

    def login_user(self, request, username, password):
        print(self)
        merchant = authenticate(username=username, password=password)
        if merchant:
            login(request, merchant)
            return True
        return False

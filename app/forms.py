from django.forms import ModelForm
from app.models import *
from django import forms



class CausesForm(ModelForm):
    name = forms.CharField(max_length=2000, required=True, label="Name",
                           widget=forms.TextInput(attrs={'id': 'name', 'name': 'name', 'class': "form-control",
                                                         'required data-error': "Please enter your name",
                                                         'placeholder': "Name"}))
    description = forms.CharField(max_length=5000, required=True, label="Name",
                                  widget=forms.Textarea(
                                      attrs={'id': 'description', 'name': 'description', 'class': "form-control",
                                             'required data-error': "Please enter the description",
                                             'placeholder': "Description", "cols": "30", "rows": "6"}))

    hospital_address = forms.CharField(max_length=1000, required=True, label="Name",
                                       widget=forms.TextInput(
                                           attrs={'id': 'hospital_address', 'name': 'hospital_address',
                                                  'class': "form-control",
                                                  'required data-error': "Please enter the hospital address",
                                                  'placeholder': "Hospital Address"}))

    target = forms.DecimalField(required=True, label="Name",
                                widget=forms.NumberInput(
                                    attrs={'id': 'target', 'name': 'target',
                                           'class': "form-control",
                                           'required data-error': "Please enter the target_amount",
                                           'placeholder': "₦ Target Amount"}))

    class Meta:
        model = Cause
        fields = ['name', 'description', 'target']

        labels = {
            'name': forms.TextInput(attrs={'id': 'name', 'name': 'name', 'class': "form-control",
                                           'required data-error': "Please enter your name", 'placeholder': "Name"}),
            'description': forms.TextInput(attrs={'id': 'description', 'name': 'description', 'class': "form-control",
                                                  'required data-error': "Please enter the description",
                                                  'placeholder': "Description"}),
            'hospital_address': forms.TextInput(
                attrs={'id': 'hospital_address', 'name': 'hospital_address', 'class': "form-control",
                       'required data-error': "Please enter the hospital address", 'placeholder': "Description"}),
            # 'image': forms.TextInput(attrs={'id': 'product_image'}),
            'target': forms.Select(attrs={'id': 'name', 'name': 'name', 'class': "form-control",
                                          'required data-error': "Please enter the target", 'placeholder': "Target"}),
        }

    def send_email(self):
        # send email using the self.cleaned_data dictionary
        return


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['body', 'name', 'email', 'blog_post']
        widgets = {
            'body': forms.TextInput(attrs={
                'id': 'post-body',
                'required': True,
                'placeholder': 'Say something...'
            }),
            'name': forms.TextInput(attrs={
                'id': 'post-name',
                'required': True,
                'placeholder': 'Say something...'}),
            'email': forms.TextInput(attrs={
                'id': 'post-text',
                'required': True,
                'placeholder': 'Say something...'
        })
        }



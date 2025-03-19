import re

from django import  forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *


from .models import Categories


# class NewsForm(forms.Form):
#     title =forms.CharField(max_length=155, label='nomlanish',
#                             widget=forms.TimeInput(attrs={"class":"form-control"}))
#     context=forms.CharField(label='text',required=False,widget=forms.Textarea(attrs={
#         "class":"form-control",
#     }))
#
#     is_bool=forms.BooleanField(label='opuvlik',initial=True)
#     category=forms.ModelChoiceField(empty_label='kategory tanlang',
#                                 label='category',queryset=Categories.objects.all(),
#                                 widget=forms.Select(attrs={"class":"from-control"}))


class NewsForms(forms.ModelForm):
    class Meta:
        model=News
        fields=['title','context','is_bool','category']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'context':forms.Textarea(attrs={'class':'form-control', 'rows':5}),
            'category':forms.Select(attrs={'class':'form-control'}),


        }

    video = forms.FileField(
        required=False,
        widget=forms.ClearableFileInput(attrs={'class': 'form-control', 'accept': 'video/*'})
    )



    def clean_title(self):
        title=self.cleaned_data['title']
        if re.match(r'\d',title):
            raise ValidationError('nazifanie ne doljin ')
        return title
class UserLoginForm(AuthenticationForm):
    username = forms.CharField(label='login',widget=forms.TextInput(attrs={'class':'form-control'})),
    password = forms.CharField(label='login',widget=forms.PasswordInput(attrs={'class':'form-control'})),
    class Meta:
        model=User
        fields=('username','password',)































#
# from django import forms
# from .models import *
#
#
# class NewsForm(forms.Form):
#     title = forms.CharField(max_length=150, label='Название', widget=forms.TextInput(attrs={"class": 'form-control'}))
#
#     context = forms.CharField(label='Текст', required=False, widget=forms.Textarea(attrs={"class": 'form-control', "rows": 5}))
#     is_bool = forms.BooleanField(label='Опубликовано?', initial=True)
#
#     category = forms.ModelChoiceField(empty_label='Выберите категории', label='Категория',
#                                       queryset=Categories.objects.all(),
#                                       widget=forms.Select(attrs={"class": "form-control"}))
#
# class CategoryForm(forms.Form):
#     title = forms.CharField(max_length=40, label='Название', widget=forms.TextInput(attrs={"class": 'form-control'}))
#
#

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, PasswordChangeForm
from django.core.exceptions import ValidationError
from django.forms import Textarea, TextInput

from .models import Client, Book


class RegisterForm(UserCreationForm):
    # fields we want to include and customize in our form
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Имя',
                                                               'class': 'form-control',
                                                               'id': "first-name",
                                                               }))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Фамилия',
                                                              'class': 'form-control',
                                                              'id': "last-name",
                                                              }))
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя Пользователя',
                                                             'class': 'form-control',
                                                             'id': "username",
                                                             }))
    email = forms.EmailField(max_length=100,
                             required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Электронная почта',
                                                           'class': 'form-control',
                                                           'id': "email",
                                                           }))
    password1 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password1',
                                                                  }))
    password2 = forms.CharField(max_length=50,
                                required=True,
                                widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите Пароль',
                                                                  'class': 'form-control',
                                                                  'data-toggle': 'password',
                                                                  'id': 'password2',
                                                                  }))

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data.get('username') == 'hi':
            raise ValidationError('Unknown username!')

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']  # 'vk_link',


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя Пользователя',
                                                             'class': 'form-control',
                                                             'id': 'nameuser',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))

    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=150, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': "Enter your last name"}))

    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': "Enter uour username"}))

    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your first name"}))

    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Enter your last name"}))

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email']


class UpdateProfileForm(forms.ModelForm):
    vk_link = forms.URLField(max_length=100,
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Client
        fields = ['vk_link']


class PasswordChangingForm(PasswordChangeForm):
    old_password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'New Passowrd'}))
    new_password2 = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'class': 'form-control', 'placeholder': 'Conform new password', 'style': "margin-bottom: 70px;"}))

    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'genre']

        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'author': TextInput(attrs={'class': 'form-control'}),
            'genre': TextInput(attrs={'class': 'form-control', 'style': 'margin-bottom: 70px'}),
        }


class ForgotPasswForm(forms.Form):
    email = forms.EmailField(max_length=100,
                             required=True,
                             widget=forms.TextInput(attrs={'placeholder': 'Электронная почта',
                                                           'class': 'form-control',
                                                           'id': "email",
                                                           }))

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

from .models import Client, Book


# class RegisterForm(UserCreationForm):
#     # fields we want to include and customize in our form
#     first_name = forms.CharField(max_length=100,
#                                  required=True,
#                                  widget=forms.TextInput(attrs={'placeholder': 'Имя',
#                                                                'class': 'form-control',
#                                                                }))
#     last_name = forms.CharField(max_length=100,
#                                 required=True,
#                                 widget=forms.TextInput(attrs={'placeholder': 'Фамилия',
#                                                               'class': 'form-control',
#                                                               }))
#     username = forms.CharField(max_length=100,
#                                required=True,
#                                widget=forms.TextInput(attrs={'placeholder': 'Имя Пользователя',
#                                                              'class': 'form-control',
#                                                              }))
#     vk_link = forms.URLField(required=True,
#                                widget=forms.URLInput(attrs={'placeholder': 'VK ссылка',
#                                                             'class': 'form-control',
#                                                             }))
#     password1 = forms.CharField(max_length=50,
#                                 required=True,
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
#                                                                   'class': 'form-control',
#                                                                   'data-toggle': 'password',
#                                                                   'id': 'password',
#                                                                   }))
#     password2 = forms.CharField(max_length=50,
#                                 required=True,
#                                 widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите Пароль',
#                                                                   'class': 'form-control',
#                                                                   'data-toggle': 'password',
#                                                                   'id': 'password',
#                                                                   }))
#
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'vk_link', 'password1', 'password2']
#
class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'first_name',
            'last_name',
            'username',
            # 'vk_link',
            # 'email',
            'password1',
            'password2',
        ]
    def save(self, commit=True):
         user = super(RegisterForm, self).save(commit=False)
         user.first_name = self.cleaned_data['first_name']
         user.last_name = self.cleaned_data['last_name']
         # user.email = self.cleaned_data['email']

         if commit:
             user.save()

         return user


class EditForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = [
            'first_name',
            'last_name',
            'vk_link',
       ]


class LoginForm(AuthenticationForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'placeholder': 'Имя Пользователя',
                                                             'class': 'form-control',
                                                             }))
    password = forms.CharField(max_length=50,
                               required=True,
                               widget=forms.PasswordInput(attrs={'placeholder': 'Пароль',
                                                                 'class': 'form-control',
                                                                 'data-toggle': 'password',
                                                                 'id': 'password',
                                                                 'name': 'password',
                                                                 }))
    remember_me = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password', 'remember_me']


class UpdateUserForm(forms.ModelForm):
    username = forms.CharField(max_length=100,
                               required=True,
                               widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['username']


class UpdateProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100,
                                 required=True,
                                 widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(max_length=100,
                                required=True,
                                widget=forms.TextInput(attrs={'class': 'form-control'}))
    vk_link = forms.URLField(max_length=100,
                             required=True,
                             widget=forms.TextInput(attrs={'class': 'form-control'}))

    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'vk_link']


class AddBookForm(forms.ModelForm):
    class Meta:
        model = Book
        # fields = '__all__'
        fields = ['title', 'author', 'genre']

        # widgets={}


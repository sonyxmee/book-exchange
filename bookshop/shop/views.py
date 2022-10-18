from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.views.generic import CreateView, ListView

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, AddBookForm
from .utils import DataMixin
from .models import Book


@login_required
def home(request):
    return render(request, 'shop/home.html')

class BookView(DataMixin, ListView):
    model = Book
    template_name = 'shop/index.html'
    context_object_name = 'prod'

    # def get_queryset(self):
    #     return Product.objects.filter(cost__gte=1500)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Список товаров')
        return context | c_def

class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'shop/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect(to='/')

        # else process dispatch as it otherwise normally would
        return super(RegisterView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            messages.success(request, f'Аккаунт создан для {username}')

            return redirect(to='login')

        return render(request, self.template_name, {'form': form})


# Class based view that extends from the built in login view to add a remember me functionality
class CustomLoginView(LoginView):
    form_class = LoginForm

    def form_valid(self, form):
        remember_me = form.cleaned_data.get('remember_me')

        if not remember_me:
            # set session expiry to 0 seconds. So it will automatically close the session after the browser is closed.
            self.request.session.set_expiry(0)

            # Set session as modified to force data updates/cookie to be saved.
            self.request.session.modified = True

        # else browser session will be as long as the session cookie time "SESSION_COOKIE_AGE" defined in settings.py
        return super(CustomLoginView, self).form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'shop/password_reset.html'
    email_template_name = 'shop/password_reset_email.html'
    subject_template_name = 'shop/password_reset_subject'
    success_message = "Инструкция по изменению пароля были отправлены Вам на почту, " \
                      " если Вы не получили письмо, " \
                      "проверьте папку Спам и корректность введенного адреса почты."
    success_url = reverse_lazy('shop-home')


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'shop/change_password.html'
    success_message = "Пароль был успешно изменен"
    success_url = reverse_lazy('shop-home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль был успешно изменен')
            return redirect(to='shop-profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'shop/profile.html', {'user_form': user_form, 'profile_form': profile_form})


class AddBook(DataMixin, CreateView):
    form_class = AddBookForm
    template_name = 'shop/addBook.html'

    success_url = reverse_lazy('home')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title='Добавить книгу')
        return context | c_def

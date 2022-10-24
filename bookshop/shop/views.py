from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, AddBookForm, PasswordChangingForm
from .utils import DataMixin
from .models import Book, Client


@login_required
def home(request):
    return render(request, 'shop/home.html')


class BookView(ListView):  # DataMixin,
    model = Book
    template_name = 'shop/listbook.html'
    context_object_name = 'prod'

    def get_queryset(self):
        return Book.objects.filter(client__user=self.request.user)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Список книг'
        return context


class AddBook(CreateView):  # DataMixin,
    form_class = AddBookForm
    template_name = 'shop/addBook.html'
    success_url = reverse_lazy('listbook')

    def form_valid(self, form):
        # создаем форму, но не отправляем его в БД, пока просто держим в памяти
        fields = form.save(commit=False)
        # Через реквест передаем недостающую форму, которая обязательна
        fields.client = Client.objects.get(user=self.request.user)
        # Наконец сохраняем в БД
        # fields.save()
        return super().form_valid(form)

    #
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     c_def = self.get_user_context(title='Добавить книгу')
    #     return context | c_def


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
            messages.success(request, f'Account created for {username}')
            # неуверена, так ли делать возврат на домашнюю страницу после успешной регистрации
            return redirect('home')
            # return redirect(to='api/home')

        return render(request, self.template_name, {'form': form})


class UpdatePublicDetails(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = "upd_profile"
    form_class = UpdateProfileForm
    template_name = "shop/edit_profile.html"
    success_url = reverse_lazy('home')
    success_message = "User updated"

    def get_object(self):
        return self.request.user.profile

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR, "Please submit the form carefully")
        return redirect('home')


class UpdateUserDetails(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = "upd_user"
    form_class = UpdateUserForm
    template_name = "shop/edit_user.html"
    success_url = reverse_lazy('home')
    success_message = "User updated"

    def get_object(self):
        return self.request.user

    def form_invalid(self, form):
        messages.add_message(self.request, messages.ERROR,
                             "Please submit the form carefully")
        return redirect('home')


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
    success_url = reverse_lazy('home')



class PasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    form_class = PasswordChangingForm
    login_url = 'change_passw'
    success_url = reverse_lazy('password_success')


def password_success(request):
    return render(request, "shop/change_passw_success.html")

# @login_required
# def profile(request):
#     if request.method == 'POST':
#         user_form = UpdateUserForm(request.POST, instance=request.user)
#         profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)
#
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, 'Профиль был успешно изменен')
#             return redirect(to='profile')
#     else:
#         user_form = UpdateUserForm(instance=request.user)
#         profile_form = UpdateProfileForm(instance=request.user.profile)
#
#     return render(request, 'shop/profile.html', {'user_form': user_form, 'profile_form': profile_form})

class Profile(LoginRequiredMixin, View):
    model = Client
    login_url = 'profile'
    template_name = "shop/profile.html"

    def get(self, request, ):
        user_profile_data = Client.objects.get(user=request.user.id)
        context = {
            'user_profile_data': user_profile_data
        }
        return render(request, self.template_name, context)

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, PasswordResetView, PasswordChangeView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views import View
from django.views.generic import CreateView, ListView, DetailView

from .forms import RegisterForm, LoginForm, UpdateUserForm, UpdateProfileForm, AddBookForm, EditForm
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


class ShowBook(DetailView):
    model = Book
    template_name = 'shop/showbook.html'
    context_object_name = 'book'
    # slug_url_kwarg = 'book_slug'


class RegisterView(View):
    form_class = RegisterForm
    initial = {'key': 'value'}
    template_name = 'shop/register.html'

    def dispatch(self, request, *args, **kwargs):
        # will redirect to the home page if a user tries to access the register page while logged in
        if request.user.is_authenticated:
            return redirect('home')

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
            return redirect('home')

        return render(request, self.template_name, {'form': form})


# class CreateProfileView(CreateView):
#     model = Client
#
#     template_name = 'shop/register.html'
#     fields = ['first_name', 'last_name', 'vk_link', 'password1', 'password2']
#
#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)
#
#     success_url = reverse_lazy('home')

def register(request):
    # pylint: disable=maybe-no-member
    form = RegisterForm()
    if request.method == 'POST':

        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Account was created for ' + user)
            return redirect('register_profile')

    else:
        form = RegisterForm()

    return render(request, 'shop/register.html', {'form': form})


def RegisterPage(request):
    if request.method == 'POST':

        form = EditForm(request.POST,
                        request.FILES,
                        instance=request.user.profileuser)

        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile has been updated!')
            return redirect('home')

        else:
            messages.error(request, 'Update failed. Please check if your inputs are valid.')

    else:
        form = EditForm(instance=request.user.profileuser)

    context = {
        'form': form,
        'on_profile_page': True
    }
    return render(request, '', context)


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


class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'shop/change_password.html'
    success_message = "Пароль был успешно изменен"
    success_url = reverse_lazy('home')


@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = UpdateProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль был успешно изменен')
            return redirect(to='profile')
    else:
        user_form = UpdateUserForm(instance=request.user)
        profile_form = UpdateProfileForm(instance=request.user.profile)

    return render(request, 'shop/profile.html', {'user_form': user_form, 'profile_form': profile_form})

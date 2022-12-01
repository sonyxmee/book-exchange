from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .views import *
from .forms import LoginForm

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, authentication_form=LoginForm),
    #      name='login'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='shop/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='shop/logout.html'), name='logout'),
    # path('password_reset/', ForgotPasswordView.as_view(), name='password_reset'),
    path('password_reset/', forgot_passw, name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='shop/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='shop/password_reset_complete.html'),
         name='password_reset_complete'),
    path('change_password', PasswordChangeView.as_view(template_name="shop/change_password.html"), name='change_passw'),
    path('password_success/', password_success, name="password_success"),
    path('upd_profile/', UpdatePublicDetails.as_view(), name='upd_profile'),
    path('upd_user/', UpdateUserDetails.as_view(), name='upd_user'),
    path('profile/', Profile.as_view(), name='profile'),
    path('listbook/', BookView.as_view(), name='listbook'),
    # path('register/', RegisterView.as_view(), name='register'),
    path('addbook/', AddBook.as_view(), name='addbook'),
    path('delete_book/<book_id>', BookView.delete_book, name='delete-book'),
    path('home/', home, name='home'),
    path('', main, name='main'),
    path('edit_info/', edit_info, name='edit_info'),

]

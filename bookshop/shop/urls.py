from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *
from .forms import LoginForm

urlpatterns = [
    # path('register/', RegisterView.as_view(), name='register'),
    path('register/', register, name='register'),
    path('register_profile/', RegisterPage, name='register_profile'),
    path('login/', CustomLoginView.as_view(redirect_authenticated_user=True, template_name='shop/login.html',
                                           authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='shop/logout.html'), name='logout'),
    path('password-reset/', ResetPasswordView.as_view(), name='password_reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(template_name='shop/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(template_name='shop/password_reset_complete.html'),
         name='password_reset_complete'),
    path('profile/', profile, name='profile'),
    path('listbook/', BookView.as_view(), name='listbook'),
    path('books/<int:pk>/', ShowBook.as_view(), name='bookdetail'),
    # path('register/', RegisterView.as_view(), name='register'),
    path('addbook/', AddBook.as_view(), name='addbook'),
    path('home/', home, name='home'),

]
from django.urls import path
from .views import *

urlpatterns = [
    path('home/', home, name='shop-home'),
    path('register/', RegisterView.as_view(), name='shop-register'),
    path('profile/', profile, name='shop-profile'),
]
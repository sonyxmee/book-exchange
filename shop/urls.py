from django.urls import path
from .views import *

urlpatterns = [
    # path('profile/', profile, name='users-profile'),
    path('home/', home, name='home'),
]
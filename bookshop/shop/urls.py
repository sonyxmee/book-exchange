from django.urls import path
from .views import *

urlpatterns = [
    # path('profile/', profile, name='users-profile'),
    path('home/', BookView.as_view(), name='home'),
    # path('register/', RegisterView.as_view(), name='register'),
    path('addbook/', AddBook.as_view(), name='addbook'),

]
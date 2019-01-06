from django.urls import path
from .views import home, logout_sys


urlpatterns = [
    path('', home, name='home'),
    path('logout', logout_sys, name='logout'),
]

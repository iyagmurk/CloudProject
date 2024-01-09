# urls.py
from django.urls import path
from .views import shorten_url, redirect_to_long_url

urlpatterns = [
    path('', shorten_url, name='shorten_url'),
    path('<str:short_code>/', redirect_to_long_url, name='redirect_to_long_url'),
]

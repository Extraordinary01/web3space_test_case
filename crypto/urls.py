from django.urls import path
from .views import index, cryptorank_view, coingecko_view

urlpatterns = [
    path('', index, name='home'),
    path('cryptorank', cryptorank_view, name='cryptorank'),
    path('coingecko', coingecko_view, name='coingecko')
]

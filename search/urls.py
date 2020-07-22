from django.urls import path
from . import views

app_name = 'search'

urlpatterns = [
    path('client', views.search_client, name='search_client'),
    path('house', views.search_house, name='search_house'),
]

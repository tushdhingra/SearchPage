from django.urls import include, path
from . import views

app_name = 'SearchApp'

urlpatterns = [
    path('', views.index),
]


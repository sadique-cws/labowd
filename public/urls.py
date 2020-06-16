
from django.contrib import admin
from django.urls import path,include
from public.views import *
urlpatterns = [
    path('',HomeView.as_view(),name='homepage'),
]

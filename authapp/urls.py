from django.urls import path,include
from .views import *

app_name = 'authapp'

urlpatterns = [
    path('',HomeView.as_view(),name='home')
]
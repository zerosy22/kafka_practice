from django.urls import path
from .views import helloAPI, signupAPI
from . import views

urlpatterns = [
    path("hello/", helloAPI),
    path("signup/", signupAPI),
]
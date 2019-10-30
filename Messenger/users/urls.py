from django.urls import path

from . import views

urlpatterns = [
    path('add', views.user_add),
    path('login', views.login)
]
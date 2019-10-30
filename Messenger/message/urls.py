from django.urls import path

from . import views

urlpatterns = [
    path('', views.chat),
    path('<int:user_id>', views.chat),
    path('message/new', views.add_message)
]
from django.urls import path
from connect import views

urlpatterns = [
    path("", views.home, name='home'),
    path("create/<str:username>", views.video, name='create'),
]
from django.urls import path
from connect import views

urlpatterns = [
    path("", views.home, name='home'),
    path("connection/<str:username>", views.connection, name='connection'),
]

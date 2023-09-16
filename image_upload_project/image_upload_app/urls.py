from django.urls import path

from . import views

urlpatterns = [
    path("user-detail/<int:id>", views.user_detail, name="user-detail"),
]
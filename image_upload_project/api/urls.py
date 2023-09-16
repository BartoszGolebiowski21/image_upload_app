from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('images/', views.get_images),
    path('images/<int:pk>', views.get_image),
    path('users/', views.get_users),
    path('users/<int:pk>', views.get_user),
    path('tiers/', views.get_tiers),
    path('tiers/<int:pk>', views.get_tier),
]
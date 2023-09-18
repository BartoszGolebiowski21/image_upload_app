from django.urls import path
from . import views

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('', views.get_routes),
    path('images/', views.get_images),
    path('images/<int:pk>', views.get_image),
    path('images/upload/', views.upload_image, name='upload_image'),
    path('users/', views.get_users),
    path('users/<int:pk>', views.get_user),
    path('tiers/', views.get_tiers),
    path('tiers/<int:pk>', views.get_tier),
]
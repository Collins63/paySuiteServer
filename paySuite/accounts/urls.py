from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('api/login/', views.login_user, name='login_user'),
    path('api/logout/', views.logout_api, name='logout_api'),
]

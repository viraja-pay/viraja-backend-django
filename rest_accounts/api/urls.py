from django.urls import path

from rest_accounts.api import views


urlpatterns = [
    path('token/', views.TokenAPIView.as_view(), name="token_api_view"),
    path('create_user/', views.UserCreateAPIView.as_view(), name="API_signup"),
]

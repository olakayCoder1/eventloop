from django.urls import path
from . import views

urlpatterns = [ 
    path('account/register/', views.UserRegistrationApiView.as_view(), name='account_registration'),
    path('password/forget/', views.ResetPasswordRequestEmailApiView.as_view(), name='password_reset_request_email'),
    path('password/reset/<str:token>/<str:uuidb64>/', views.SetNewPasswordTokenCheckApi.as_view(), name='password_reset_done'),
    path('password/reset/', views.ChangePasswordView.as_view(), name='password_change'),
    path('search', views.ChangePasswordView.as_view(), name='password_change'),
]
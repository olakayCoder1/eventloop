from django.urls import path
from . import views

urlpatterns = [ 
    path('account/register', views.UserRegistrationApiView.as_view(), name='account_registration'),
    path('account/login', views.UserLogin.as_view(), name='account_login'),
    path('password/forget', views.ResetPasswordRequestEmailApiView.as_view(), name='password_reset_request_email'),
    path('password/reset/<str:token>/<str:uuidb64>/', views.SetNewPasswordTokenCheckApi.as_view(), name='password_reset_done'),
    path('password/reset', views.ChangePasswordView.as_view(), name='password_change'),
    path('search', views.ChangePasswordView.as_view(), name='password_change'),


    path('events/categories/', views.EventCentreCategoriesApiView.as_view(), name='event_centre_categories'),
    path('events', views.EventCentreApiView.as_view(), name='event_centre'),
    path('events/1', views.EventCentreCreateApiView.as_view(), name='event_centre'),
    path('events/book', views.EventCentreBookingApiView.as_view(), name='event_centre_book'),
    path('events/book/payment/', views.PaymentTransactionApiView.as_view(), name='event_centre_book_payment'),
]  
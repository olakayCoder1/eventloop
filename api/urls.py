from django.urls import path
from . import views

urlpatterns = [ 

    # AUTHENTICATION ENDPOINTS
    path('account/register', views.UserRegistrationApiView.as_view(), name='account_registration'),
    path('account/login', views.UserLogin.as_view(), name='account_login'),
    path('password/forget', views.ResetPasswordRequestEmailApiView.as_view(), name='password_reset_request_email'),
    path('password/reset/<str:token>/<str:uuidb64>', views.SetNewPasswordTokenCheckApi.as_view(), name='password_reset_done'),
    path('password/reset', views.ChangePasswordView.as_view(), name='password_change'),

    
    # EVENT ENDPOINTS
    path('search', views.EventCentreSearchAPIView.as_view(), name='search'),
    path('events/categories', views.EventCentreCategoriesApiView.as_view(), name='event_centre_categories'),
    path('events', views.EventCentreListCreateApiView.as_view(), name='event_centre_list_create'),
    path('events/<str:public_id>', views.EventCentreRetrieveDestroyApiView.as_view(), name='event_centre_retrieve_destroy'),
    path('halls', views.HallsListCreateApiView.as_view(), name='halls'),
    path('halls/<int:pk>', views.HallRetrieveDestroyApiView.as_view(), name='hall_retrieve_destroy'),

    # BOOKINGS ENDPOINT
    path('bookings', views.BookingsListCreateApiView.as_view(), name='bookings'),
    path('bookings/<int:pk>', views.BookingsRetrieveUpdateDestroyApiView.as_view(), name='bookings_retrieve'),
]  
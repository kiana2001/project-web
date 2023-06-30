from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token
from .views import ReservationCreateAPIView

urlpatterns = [
   # path('flights/', FlightList.as_view(), name='flight-list'),
   # path('flights/<int:pk>/', FlightDetail.as_view(), name='flight-detail'),
    path('reservations/', ReservationCreateAPIView.as_view(), name='reservation-list'),
   # path('reservations/<int:pk>/', ReservationDetail.as_view(), name='reservation-detail'),
]
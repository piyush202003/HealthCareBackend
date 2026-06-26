from django.urls import path
from .views import *

urlpatterns = [
    path( "", DoctorListCreateView.as_view(), name = 'doctor-list-create'),
    path("<int:doctor_id>/", DoctorsDetailView.as_view(), name = 'doctor-detail'),
]
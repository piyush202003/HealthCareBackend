from django.urls import path
from .views import *

urlpatterns = [
    path("", PatientListCreateView.as_view(), name = "patient-list-creaate"),
    path("<int:patient_id>/", PatientDetailesView.as_view(), name = 'patient-detail'),
]
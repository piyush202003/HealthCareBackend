from django.urls import path
from .views import *

urlpatterns = [
    path("", MappingListCreateView.as_view(), name = 'mapping-list-create'),
    path("<int:patient_id>/", PatientDoctorsViews.as_view(), name = 'patient-doctor'),
    path("delete/<int:mapping_id>/", MappingDeleteView.as_view(), name = 'mapping-delete'),
]
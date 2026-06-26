from rest_framework import serializers
from .models import PatientDoctorMapping
from patients.models import Patient
from doctors.models import Doctor

class PatientDoctorMappingSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientDoctorMapping
        fields = [ "id", "patient", "doctor", "assigned_at", ]
        read_only_fields = [ "id", "assigned_at", ]
        depth = 1
        
from attr import field, fields
from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = [ "id", "first_name", "last_name", "specialization", "experience", "phone", "email", "created_at", "updated_at" ]
        read_only_fields = [ "id", "created_at", "updated_at" ]
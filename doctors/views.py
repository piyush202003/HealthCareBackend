from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from yaml import serialize

from .models import Doctor
from .serializers import DoctorSerializer

# Create your views here.
class DoctorListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many = True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DoctorSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(created_by = request.user)
        return Response(
            serializer.data,
            status = status.HTTP_201_CREATED
        )
    
class DoctorsDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, doctor_id):
        return get_object_or_404(
            Doctor,
            id = doctor_id
        )
    
    def get(self, request, doctor_id):
        doctor = self.get_object(doctor_id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    
    def put(self, request, doctor_id):
        doctor = self.get_object(doctor_id)
        serializer = DoctorSerializer( doctor, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, doctor_id):
        doctor = self.get_object(doctor_id)
        doctor.delete()
        return Response(
            {"message" : "Doctor deleted successfully"},
            status = status.HTTP_204_NO_CONTENT
        )
from django.shortcuts import render
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Patient
from .serializers import PatientSerializer

# Create your views here.
class PatientListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # if not request.user.is_staff:
        #     return Response(
        #         {"error" : "Only admins can get list of patients"}
        #         status = status.HTTP_403_FORBIDDEN
        #     )

        patients = Patient.objects.filter(created_by = request.user)
        serializer = PatientSerializer(patients, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        # if not request.user.is_staff:
        #     return Response(
        #         {"error": "Only admin can create patients"}
        #     )

        serializer = PatientSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save(created_by = request.user)

        return Response(
            serializer.data,
            status = status.HTTP_201_CREATED
        )
    
class PatientDetailesView(APIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, patient_id, user):
        return get_object_or_404(
            Patient,
            id = patient_id,
            created_by = user
        )
    
    def get(self, request, patient_id):
        patient = self.get_object(patient_id, request.user)
        serializer = PatientSerializer(patient)
        return Response(serializer.data)
    
    def put(self, request, patient_id):
        patient = self.get_object(patient_id, request.user)
        serializer = PatientSerializer(patient, data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, patient_id):
        patient = self.get_object(patient_id, request.user)
        patient.delete()
        return Response(
            {
                "message" : "Paitent deleted Successfully"
            },
            status = status.HTTP_204_NO_CONTENT
        )


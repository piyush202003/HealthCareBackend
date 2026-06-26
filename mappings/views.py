from django.shortcuts import render,get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer

# Create your views here.
class MappingListCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = PatientDoctorMappingSerializer(data = request.data)
        serializer.is_valid(raise_exception = True)
        serializer.save()
        return Response(
            serializer.data,
            status = status.HTTP_201_CREATED
        )
    
    def get(self, request):
        mappings = PatientDoctorMapping.objects.select_related( "patient", "doctor" )
        serializer = PatientDoctorMappingSerializer(mappings, many = True)
        return Response(serializer.data)
    
class PatientDoctorsViews(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, patient_id):
        mappings = PatientDoctorMapping.objects.filter( patient_id = patient_id ).select_related( "doctor" )
        serializer = PatientDoctorMappingSerializer(mappings, many = True)
        return Response(serializer.data)
    
class MappingDeleteView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, mapping_id):
        mapping = get_object_or_404(PatientDoctorMapping, id = mapping_id)
        mapping.delete()
        return Response(
            {"message" : "Doctor removed from patient successfully."},
            status = status.HTTP_204_NO_CONTENT
        )
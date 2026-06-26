from django.contrib import admin
from .models import PatientDoctorMapping

# Register your models here.
@admin.register(PatientDoctorMapping)
class PatientDoctorMappingAdmin(admin.ModelAdmin):
    list_display = ( 'id', 'patient', 'doctor', 'assigned_at', )
    search_fields = ( 'patient', 'doctor', )
    ordering = ( '-assigned_at', )
    readonly_fields = ( 'assigned_at', )
    fieldsets = (
        ("Patient -> Doctor Mapping", {
            "fields" : ( 'patient', 'doctor', )
        }),
        ("TimeStamp", {
            "fields" : ( 'assigned_at', )
        }),
    )
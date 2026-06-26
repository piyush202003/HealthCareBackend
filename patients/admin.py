from django.contrib import admin
from .models import Patient

# Register your models here.
@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = [ "id", "first_name", "last_name", "age", "gender", "phone", "created_by", "created_at" ]
    list_filter = ("gender", "created_at")
    search_fields = ("first_name", "last_name", "phone", "created_by__email", "created_by__username")
    ordering = ("-created_at",)
    readonly_fields = ( "created_at", "updated_at", )
    fieldsets = (
        ("Patient Information", {
            "fields": ( "created_by", "first_name", "last_name", "age", "gender", "phone", "address", )
        }),
        ("Timestamps", {
            "fields": ( "created_at", "updated_at", )
        }),
    )
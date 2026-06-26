from django.contrib import admin
from .models import Doctor

# Register your models here.
@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ( "id", "first_name", "last_name", "specialization", "experience", "phone", "email", "created_by", "created_at", )
    list_filter = ( "created_at", )
    search_fields = ( "first_name", "last_name", "phone", "created_by__email", "created_by__username", )
    ordering = ( "-created_at", )
    readonly_fields = ( "created_at", "updated_at", )
    fieldsets = (
        ("Doctor Information", {
            "fields": ( "created_by", "first_name", "last_name", "specialization", "experience", "phone", "email", )
        }),
        ("Timestamps", {
            "fields": ( "created_at", "updated_at", )
        }),
    )
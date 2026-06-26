from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Doctor(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="doctors")
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(help_text="Experience in years")
    phone = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Dr. {self.first_name} {self.last_name}"
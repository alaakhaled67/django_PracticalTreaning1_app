from django.contrib import admin

# Register your models here.
from .models import Patient,Charges,MedicalSpecialistes,Book,test
admin.site.register((Patient,Charges,MedicalSpecialistes,Book,test,))
from django.contrib import admin
from .models import Student_data

# Register your models here.
@admin.register(Student_data)
class UserAdmin(admin.ModelAdmin):
    list_display=['student_name','father_name','dob','address','city','state','pinno','mobailno','email','class_opted','marks','date_enrolled']

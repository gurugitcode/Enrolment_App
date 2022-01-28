from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Student_data(models.Model):
    student_name=models.CharField(max_length=70)
    father_name=models.CharField(max_length=70)
    dob=models.DateField(null=True,blank=True)
    address=models.CharField(max_length=70)
    city=models.CharField(max_length=70)
    state=models.CharField(max_length=70)
    pinno=models.IntegerField()
    mobailno = models.IntegerField(default='+91',validators=[MaxValueValidator(9999999999)])
    email=models.EmailField(max_length=100)
    class_opted=models.IntegerField()
    marks=models.FloatField(null=True,blank=True)
    date_enrolled=models.DateTimeField(null=True,blank=True)


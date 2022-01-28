from django import forms
from django.contrib.auth.forms import UserCreationForm ,UsernameField,AuthenticationForm
from django.contrib.auth.models import User
from .models import Student_data

# Create Student_data_form class
class Student_data_form(forms.ModelForm):
    class Meta:
        model=Student_data
        fields=['student_name','father_name','dob','address','city','state','pinno','mobailno','email','class_opted','marks','date_enrolled']
        labels={'student_name':'StudentName','father_name':'FatherName','dob':'DOB','address':'Address','city':'City','state':'State','pinno':'PinNo','mobailno':'MobailNo','email':'Email','class_opted':'Class_Opted','marks':'Marks','date_enrolled':'Date_Enrolled'}
        widgets = {'student_name':forms.TextInput(attrs={'class':'form-control'}),
        'father_name':forms.TextInput(attrs={'class':'form-control'}),
        'address':forms.TextInput(attrs={'class':'form-control'}),
        'city':forms.TextInput(attrs={'class':'form-control'}),
        'state':forms.TextInput(attrs={'class':'form-control'}),
        'pinno':forms.TextInput(attrs={'class':'form-control'}),
        'mobailno':forms.TextInput(attrs={'class':'form-control'}),
        'email':forms.EmailInput(attrs={'class':'form-control'}),
        'class_opted':forms.TextInput(attrs={'class':'form-control'}),
        'marks':forms.TextInput(attrs={'class':'form-control'}),
        'date_enrolled':forms.DateTimeInput(format='%Y-%m-%d %H:%M',attrs={'class':'form-control'}),
        'dob':forms.DateInput(format='%d/%m/%Y',attrs={'class':'form-control'}),
        }


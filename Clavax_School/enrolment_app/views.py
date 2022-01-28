from django.shortcuts import render,HttpResponseRedirect
from django.views import View

from .models import Student_data
from .forms import Student_data_form
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
class Home(View):
    tamplate_name = "home.html"
    def get(self,request):
        return render(request,self.tamplate_name)
    def post(self,request):
        return render(request,self.tamplate_name)
# Save Register form data
class SaveData(View):
    tamplate_name = "student_form.html"
    def get(self,request):
        fm=Student_data_form()
        return render(request,self.tamplate_name,{"form":fm})
    def post(self,request):
        fm=Student_data_form(request.POST)
        try:
            if fm.is_valid():
                print(fm)
                fm.save()
                messages.success(request,'Successfully Your Post uploded.')
                fm=Student_data_form()
            else:
                messages.error(request,'ENTER VALID data.....')
                fm=Student_data_form()
                # return HttpResponseRedirect('/stu_update/stu_data')
        except Exception as err:
            print(err)
        return render(request,self.tamplate_name,{'form':fm})

# Student all data View    
class StudetdataView(View):
    template_name="student_data.html"
    def get(self,request):
        Stu_id = Student_data.objects.all()
        paginator = Paginator(Stu_id, 5)  # Show 10 contacts per page.
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request,self.template_name,{'page_obj':page_obj})
        
# Update Student_data class        
class Update_post(View):
    template_name = 'student_form.html'
    def get(self,request,id):
        data = Student_data.objects.get(pk=id)
        print(data)
        post_data = Student_data_form(instance=data)
        return render(request,self.template_name,{'form':post_data})
    def post(self,request,id):
        data = Student_data.objects.get(pk=id)
        post_data = Student_data_form(request.POST,instance=data)
        if post_data.is_valid():
            post_data.save()
            post_data=Student_data_form()
            messages.success(request,'Successfully Your Post Updated.')
            return render(request,self.template_name,{'form':post_data})

# Student data View
class Student_data_Show(View):
    template_name = 'Show_data.html'
    def get(self,request,id):
        data = Student_data.objects.get(pk=id)
        return render(request,self.template_name,{'stu_data':data})
    
from django.shortcuts import render,redirect

# Create your views here.
from .models import Student
from django.views import View
from .forms import AddStudentForm

class Home(View):
    def get(self, request):
        student=Student.objects.all()
        for i in student:
            print(i.name,i.city,i.roll)
        return render(request,'core/home.html',{'student':student})


class AddStudent(View):
    def get(self,request):
        fm=AddStudentForm()
        return render(request,'core/addstudent.html',{'form':fm})

    def post(self,request):
        fm=AddStudentForm(request.POST)
        if fm.is_valid():
            fm.save()
            return redirect('/')
        else:
              return render(request,'core/addstudent.html',{'form':fm})


class Delete_Student(View):
    def post(self,request):
        data=request.POST
        id=data.get('id')
        try:
            studata=Student.objects.get(id=id)
            studata.delete()
        except:
            pass
        return redirect('/')

class EditStudent(View):
    def get(self,request,id):
        studata=Student.objects.get(id=id)
        fm=AddStudentForm(instance=studata)
        return render(request,'core/editStudent.html',{'form':fm})

    def post(self,request,id):
        studata=Student.objects.get(id=id)
        fm=AddStudentForm(request.POST,instance=studata)
        if fm.is_valid():
            fm.save()
        else:
            pass
        return redirect('/')



      
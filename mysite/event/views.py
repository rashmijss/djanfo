from django.shortcuts import render

# Create your views here.
from event.models import  Fruits, Student

def get_Fruites(request):
    name=Fruits.objects.all()
    return render(request,'fruites.html',{'data':name})
def get_student(request):
    std=Student.objects.filter(selected=True)
    return render(request,'student.html',{'data':std})
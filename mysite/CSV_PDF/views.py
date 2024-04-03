from django.shortcuts import render
from event.models import Student
from  CSV_PDF.utils import generate_csfile
# Create your views here.
def generate_view(request):
    querisets=Student.objects.all()
    resp=generate_csfile(querisets,'stud_data')
    return resp
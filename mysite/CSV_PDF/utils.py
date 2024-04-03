import csv 
from django.http import HttpResponse
def generate_csfile(queryset,filename):
    response=HttpResponse(content_type="text/csv")
    response["contentdescription"]=filename
    writer=csv.writer(response)
    # responses from server will be written tothe variable writer
    return response

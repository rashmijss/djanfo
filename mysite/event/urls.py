from django.urls import path
from . import views 
urlpatterns=[
    path('get_fruites/',views.get_Fruites),
     path('get_student/',views.get_student),
]
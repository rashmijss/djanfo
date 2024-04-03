from django.urls import path
from . import views 
urlpatterns=[
    path('get_csv/',views.generate_view),

    # we can give any name for this get 
   
]
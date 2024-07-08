from django.urls import path
from .views import * # Import your view function

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),  # Specify the view function and name
    path('',index,name='index'),
    
]

from django.urls import path
from .views import * # Import your view function

urlpatterns = [
    path('signup/',signiup,name='signup'),
    path('user/<int:pk>/dashboard/', dashboard, name='dashboard'),  # Specify the view function and name
    path('',index,name='index'),
    
]

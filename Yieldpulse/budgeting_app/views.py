from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def dashboard(request):
    pass
def index(request):
    return render(request, 'budgeting_app/index.html')
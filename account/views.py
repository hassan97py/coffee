from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def login_view(request):
    return render(request, 'account/login.html')

def register_view(request):
    return render(request, 'account/register.html')

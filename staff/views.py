from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def staff_panel(request):
    return render(request, 'staff/staff_panel.html')

def analytics(request):
    return render(request, 'staff/analytics.html')

from django.urls import path
from .views import staff_panel, analytics

urlpatterns = [
    path('staff_panel/', staff_panel, name='staff_panel'),
    path('analytics/', analytics, name='analytics'),
]

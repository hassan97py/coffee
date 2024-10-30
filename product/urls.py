from django.urls import path
from .views import menu, product_detail, home ,add_product

urlpatterns = [
    path('', home, name='home'),
    path('menu/', menu, name='menu'),
    path('product/<int:product_id>/', product_detail, name='product_detail'),
    # path('add/', add_product, name='add_product'), 
]

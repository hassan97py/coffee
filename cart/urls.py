from django.urls import path
from cart import views  

urlpatterns = [
    path('cart/', views.cart_summary, name='cart'),
    path('cart/add/', views.cart_add, name='cart_add'),
    path('cart/delete/', views.cart_delete, name='cart_delete'),
    path('cart/update/', views.cart_update, name='cart_update'),

]

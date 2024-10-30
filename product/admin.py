from django.contrib import admin

# Register your models here.
# product/admin.py
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')  # نمایش نام و قیمت در لیست
    search_fields = ('name',)  # امکان جستجو بر اساس نام محصول

admin.site.register(Product, ProductAdmin)

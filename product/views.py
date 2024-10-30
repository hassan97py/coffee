from django.shortcuts import render, redirect

# Create your views here.
from .models import Product
from .forms import ProductForm


def home(request):
    return render(request, 'product/home.html')

def menu(request):
    products = Product.objects.all()
    return render(request, 'product/menu.html', {'products': products})

def product_detail(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, 'product/product_detail.html', {'product': product})



def add_product(request):
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)  # برای بارگذاری تصاویر
        if form.is_valid():
            form.save()
            return redirect('menu')  # بعد از افزودن محصول به منو بروید
    else:
        form = ProductForm()
    
    return render(request, 'product/add_product.html', {'form': form})

from django.shortcuts import render


from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CartItem  # Assuming you have a CartItem model

def cart_summary(request):
    cart_items = CartItem.objects.all()  # Fetch all cart items
    total_price = sum(item.price for item in cart_items)  # Calculate total price
    return render(request, "cart/cart_summary.html", context={'cart_items': cart_items, 'total_price': total_price})

def cart_add(request):
    if request.method == 'POST':
        # Logic to add item to cart
        item_id = request.POST.get('item_id')
        # Add your logic to create a CartItem instance
        return redirect('cart')  # Redirect to cart summary after adding

def cart_delete(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        # Logic to delete item from cart
        CartItem.objects.filter(id=item_id).delete()
        return redirect('cart')  # Redirect to cart summary after deleting

def cart_update(request):
    if request.method == 'POST':
        item_id = request.POST.get('item_id')
        quantity = request.POST.get('quantity')
        # Logic to update item quantity in cart
        cart_item = CartItem.objects.get(id=item_id)
        cart_item.quantity = quantity
        cart_item.save()
        return redirect('cart')  # Redirect to cart summary after updating
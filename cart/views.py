from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from dxd.models import Product
from django.contrib import messages
from django.http import JsonResponse
from .cart import Cart
from .forms import CartAddProductForm
from coupons.forms import CouponApplyForm

   
@require_POST
def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    form = CartAddProductForm(request.POST)

    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,quantity=cd['quantity'], override_quantity=cd['override'])
        messages.success(request, 'Successfully added product!')
        quantity = cart.__len__()
        response = JsonResponse({'quantity': quantity})
    return redirect('cart:cart_summary')

@require_POST
def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    messages.success(request, 'Item deleted!')
    return redirect('cart:cart_summary')

def cart_summary(request):
    cart = Cart(request)
    for item in cart:
        item['update_quantity_form'] = CartAddProductForm(initial={'quantity': item['quantity'],'override': True})
    coupon_apply_form = CouponApplyForm()
    return render(request, 'pages/checkout.html', {'cart': cart, 'coupon_apply_form': coupon_apply_form})
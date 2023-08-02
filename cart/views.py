from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View
from .cart import Cart
from .forms import CartAddProductForm
from product.models import Product
from coupons.forms import CouponApplyForm


class AddCartView(View):
    def post(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, id=pk)
        form = CartAddProductForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            cart.add(product=product,
                 quantity=cd['quantity'],
                 override_quantity=cd['override'])
        return redirect('cart:cart_detail')



class RemoveCartView(View):
    def post(self, request, pk):
        cart = Cart(request)
        product = get_object_or_404(Product, id=pk)
        cart.remove(product)
        return redirect('cart:cart_detail')
    

class CartDetailView(View):
    def get(self, request):
        cart = Cart(request)
        for item in cart:
            item['update_quantity_form'] = CartAddProductForm(initial={
                            'quantity': item['quantity'],
                            'override': True})
        coupon_apply_form = CouponApplyForm()
        cart_products = [item['product'] for item in cart]

        return render(request,
                    'cart/detail.html',
                    {'cart': cart,
                    'coupon_apply_form': coupon_apply_form})
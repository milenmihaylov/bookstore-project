from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views import View

from bookworm.bookstore.models import Book
from bookworm.cart.models import CartItem
from bookworm.core.views import CategoriesNavMixin


@login_required
def add_to_cart(request, pk):
	book = Book.objects.get(pk=pk)
	cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
	if not created:
		cart_item.quantity += 1
		cart_item.save()
	return redirect('cart')


@login_required()
def remove_from_cart(request, pk):
	cart_item = CartItem.objects.get(pk=pk)
	cart_item.delete()
	return redirect('cart')


@login_required()
def cart(request):
	cart_items = CartItem.objects.filter(user=request.user)
	total_price = sum(item.book.price * item.quantity for item in cart_items)
	for item in cart_items:
		item.total = item.book.price * item.quantity
	return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total_price': total_price})


class AddToCartView(CategoriesNavMixin, LoginRequiredMixin, View):
	def post(self, request, product_id):
		book = Book.objects.get(pk=product_id)
		cart_item, created = CartItem.objects.get_or_create(user=request.user, book=book)
		if not created:
			cart_item.quantity += 1
			cart_item.save()
		return redirect('cart')


class RemoveFromCartView(CategoriesNavMixin, LoginRequiredMixin, View):
	def post(self, request, pk):
		cart_item = CartItem.objects.get(pk=pk)
		cart_item.delete()
		return redirect('cart')


class CartView(CategoriesNavMixin, LoginRequiredMixin, View):
	def get(self, request):
		cart_items = CartItem.objects.filter(user=request.user)
		total_price = sum(item.product.price * item.quantity for item in cart_items)
		for item in cart_items:
			item.total = item.book.price * item.quantity
		return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total_price': total_price})

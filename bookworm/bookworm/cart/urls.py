from django.urls import path

from bookworm.cart.views import add_to_cart, cart, remove_from_cart, AddToCartView, RemoveFromCartView, CartView

urlpatterns = [
	path('', cart, name='cart'),
	path('add/<int:pk>', add_to_cart, name='add to cart'),
	path('remove/<int:pk>', remove_from_cart, name='remove from cart'),
]

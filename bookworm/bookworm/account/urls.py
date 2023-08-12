from django.urls import path

from bookworm.account.views import ShowDashboard, AccountDetails, OrdersView, AddToWishlistView, WishlistView

urlpatterns = [
	path('', ShowDashboard.as_view(), name='dashboard'),
	path('details/', AccountDetails.as_view(), name='account details'),
	path('orders/', OrdersView.as_view(), name='orders'),
	path('add-to-wishlist/<int:pk>', AddToWishlistView.as_view(), name='add to wishlist'),
	path('wishlist/', WishlistView.as_view(), name='wishlist'),
]

import bookworm.account.signals

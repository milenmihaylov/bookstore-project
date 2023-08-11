from django.urls import path

from bookworm.account.views import ShowDashboard, AccountDetails, WishlistDetails, OrdersView

urlpatterns = [
	path('', ShowDashboard.as_view(), name='dashboard'),
	path('details/', AccountDetails.as_view(), name='account details'),
	path('wishlist/', WishlistDetails.as_view(), name='wishlist'),
	path('orders/', OrdersView.as_view(), name='orders'),
]

import bookworm.account.signals

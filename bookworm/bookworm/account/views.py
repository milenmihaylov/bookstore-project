from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, UpdateView, ListView

from bookworm.account.forms import AccountForm
from bookworm.account.models import Account
from bookworm.bookstore.models import Book, Wishlist
from bookworm.core.views import CategoriesNavMixin


class ShowDashboard(TemplateView):
	template_name = 'shop/account-dashboard.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['account'] = Account.objects.get(pk=self.request.user.id)
		return context


class AccountDetails(CategoriesNavMixin, LoginRequiredMixin, UpdateView):
	model = Account
	context_object_name = 'account'
	template_name = 'shop/account_details.html'
	form_class = AccountForm
	success_url = reverse_lazy('account details')
	slug_url_kwarg = 'user_id'

	def get_object(self, queryset=None):
		queryset = self.get_queryset()
		obj = queryset.filter(pk=self.request.user.id).first()
		return obj

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['pass_change_form'] = PasswordChangeForm(user=self.request.user)
		return context


class OrdersView(LoginRequiredMixin, TemplateView):
	template_name = 'shop/orders-all.html'


class AddToWishlistView(LoginRequiredMixin, View):
	def get(self, request, pk):
		book = Book.objects.get(pk=pk)
		wishlist_object = book.wishlist_set.filter(user=request.user).first()
		if not wishlist_object:
			Wishlist(
				book=book,
				user=request.user,
			).save()
		return redirect('book detail', pk)


@login_required
def wishlist_view(request):
	wishlist_items = Wishlist.objects.filter(user=request.user)
	return render(request, 'shop/account-wishlist.html', {'wishlist_items': wishlist_items})


class WishlistView(CategoriesNavMixin, LoginRequiredMixin, ListView):
	model = Wishlist
	template_name = 'shop/account-wishlist.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['wishlist_items'] = Wishlist.objects.filter(user=self.request.user)
		return context

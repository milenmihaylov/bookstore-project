from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, DetailView, UpdateView

from bookworm.account.forms import AccountForm
from bookworm.account.models import Account


class ShowDashboard(TemplateView):
	template_name = 'shop/account-dashboard.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['account'] = Account.objects.get(pk=self.request.user.id)
		return context

class AccountDetails(UpdateView):
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


class WishlistDetails(TemplateView):
	template_name = 'shop/account-wishlist.html'


class OrdersView(TemplateView):
	template_name = 'shop/orders-all.html'

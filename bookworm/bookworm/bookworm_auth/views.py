from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, FormView

from bookworm.bookworm_auth.forms import RegisterForm, LogInForm

USER_MODEL = get_user_model()


def register_view(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
		context = {
			'register_form': form,
		}
		return render(request, 'auth/register.html', context)
	else:
		context = {
			'register_form': RegisterForm(),
		}
		return render(request, 'auth/register.html', context)


class LoginUserView(View):  # (LoginView):
	template_name = 'auth/login.html'
	form_class = LogInForm

	def get_success_url(self):
		return reverse_lazy('account details')


class RegisterView(CreateView):
	model = USER_MODEL
	form_class = RegisterForm
	template_name = 'auth/register.html'
	success_url = reverse_lazy('login user')


class LogoutUserView(View):  # (LoginRequiredMixin, LogoutView):
	next_page = reverse_lazy('index')


class LoginGoogleView(LoginView):
	template_name = 'auth/google-login.html'
	form_class = LogInForm

	def get_success_url(self):
		return reverse_lazy('account details')

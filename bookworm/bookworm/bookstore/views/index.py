from django.core.exceptions import ValidationError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView

from bookworm.bookstore.forms import NewsletterListForm
from bookworm.bookstore.models import Author, Category, Book
from bookworm.core.views import CategoriesNavMixin


class IndexView(CategoriesNavMixin, TemplateView):
	template_name = 'home/index.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['featured_books'] = Book.objects.filter(ave_rating__gte=4.0)
		context['bestselling_books'] = Book.objects.all()
		context['favorite_authors'] = Author.objects.all()
		context['arts_category'] = Category.objects.filter(category='Arts & Photography').first()
		context['food_category'] = Category.objects.filter(category='Food & Drink').first()
		context['romance_category'] = Category.objects.filter(category='Romance').first()
		context['health_category'] = Category.objects.filter(category='Health').first()
		context['biography_category'] = Category.objects.filter(category='Biography').first()

		return context


class NewsletterSubscribeFormView(CategoriesNavMixin, FormView):
	form_class = NewsletterListForm
	template_name = 'home/index.html'
	success_url = reverse_lazy('index')

	def form_valid(self, form):
		form.save()
		return redirect('index')


class AboutUsView(CategoriesNavMixin, TemplateView):
	template_name = 'others/about.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['what_is_this'] = "A bookstore app created as a final project for the SoftUni Python web module"
		return context


class TermsAndConditionsView(CategoriesNavMixin, TemplateView):
	template_name = 'others/terms-conditions.html'


class ContactView(CategoriesNavMixin, TemplateView):
	template_name = 'others/contact.html'


class FAQView(CategoriesNavMixin, TemplateView):
	template_name = 'others/faq.html'

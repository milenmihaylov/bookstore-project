from django.http import HttpResponseNotFound
from django.views.decorators.csrf import requires_csrf_token
from django.views.defaults import ERROR_404_TEMPLATE_NAME, ERROR_PAGE_TEMPLATE

from bookworm.bookstore.forms import NewsletterListForm
from bookworm.bookstore.models import Category

from urllib.parse import quote
from django.template import Context, Engine, loader, TemplateDoesNotExist


class CategoriesNavMixin:

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		context['categories'] = Category.objects.all()
		context['newsletter_form'] = NewsletterListForm
		return context


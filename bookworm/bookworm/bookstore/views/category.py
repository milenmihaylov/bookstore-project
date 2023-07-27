from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView

from bookworm.bookstore.forms import CategoryCreateForm
from bookworm.bookstore.models import Category
from bookworm.core.views import CategoriesNavMixin


class CategoryCreateView(CategoriesNavMixin, CreateView):
	model = Category
	template_name = 'create-category.html'
	fields = '__all__'
	success_url = reverse_lazy('index')


class CategoryListView(CategoriesNavMixin, ListView):
	model = Category
	template_name = 'all-categories.html'
	context_object_name = 'categories'


class CategoryUpdateView(CategoriesNavMixin, UpdateView):
	model = Category
	template_name = 'update-category.html'
	fields = '__all__'
	success_url = reverse_lazy('all categories')


class CategoryDeleteView(CategoriesNavMixin, DeleteView):
	model = Category
	template_name = 'delete-category.html'
	success_url = reverse_lazy('all categories')


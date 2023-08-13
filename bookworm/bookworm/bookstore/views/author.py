from os.path import join

from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, DetailView, ListView, UpdateView, DeleteView

from bookworm import settings
from bookworm.bookstore.forms import AuthorForm
from bookworm.bookstore.models import Author
from bookworm.core.clean_up import clean_up_files
from bookworm.core.mixins import StaffOnlyTestMixin
from bookworm.core.views import CategoriesNavMixin


class AuthorCreateView(CategoriesNavMixin, StaffOnlyTestMixin, CreateView):
	model = Author
	template_name = 'create-author.html'
	form_class = AuthorForm

	def get_success_url(self):
		return reverse_lazy('author detail', kwargs={'pk': self.object.id})


class AuthorDetailView(CategoriesNavMixin, DetailView):
	model = Author
	template_name = 'others/authors-single.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		context['books'] = self.object.book_set.all()
		return context


class AuthorsListView(CategoriesNavMixin, ListView):
	model = Author
	template_name = 'others/authors-list.html'
	context_object_name = 'authors'


class AuthorUpdateView(CategoriesNavMixin, StaffOnlyTestMixin, UpdateView):
	model = Author
	template_name = 'update-author.html'
	form_class = AuthorForm

	def form_valid(self, form):
		old_image = self.get_object().image
		new_image = self.request.FILES.get('image')
		if old_image and new_image:
			clean_up_files(join(settings.MEDIA_ROOT, str(old_image)))
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy('author detail', kwargs={'pk': self.object.id})


class AuthorDeleteView(CategoriesNavMixin, StaffOnlyTestMixin, DeleteView):
	model = Author
	template_name = 'delete-author.html'
	success_url = reverse_lazy('authors list')

	def form_valid(self, form):
		instance_image = self.get_object().image
		if instance_image:
			clean_up_files(join(settings.MEDIA_ROOT, str(instance_image)))
		return super().form_valid(form)

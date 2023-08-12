from os.path import join

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from bookworm import settings
from bookworm.blog.models import Article
from bookworm.core.clean_up import clean_up_files
from bookworm.core.mixins import StaffOnlyTestMixin
from bookworm.core.views import CategoriesNavMixin


class BlogListView(CategoriesNavMixin, ListView):
	model = Article
	context_object_name = 'blog'
	template_name = 'blog/blog.html'


class ArticleDetailView(CategoriesNavMixin, DetailView):
	model = Article
	template_name = 'blog/article-single.html'
	context_object_name = 'article'


class ArticleCreateView(CategoriesNavMixin, StaffOnlyTestMixin, CreateView):
	model = Article
	template_name = 'blog/create-article.html'
	fields = '__all__'

	def get_success_url(self):
		return reverse_lazy('article', kwargs={'pk': self.object.id})


class ArticleUpdateView(CategoriesNavMixin, StaffOnlyTestMixin, UpdateView):
	model = Article
	template_name = 'blog/update-view.html'
	fields = '__all__'

	def get_success_url(self):
		return reverse_lazy('article', kwargs={'pk': self.object.id})


class ArticleDeleteView(CategoriesNavMixin, StaffOnlyTestMixin, DeleteView):
	model = Article
	template_name = 'blog/delete-article.html'
	success_url = reverse_lazy('blog')

	def form_valid(self, form):
		instance_image = self.get_object().image
		if instance_image:
			clean_up_files(join(settings.MEDIA_ROOT, str(instance_image)))
		return super().form_valid(form)


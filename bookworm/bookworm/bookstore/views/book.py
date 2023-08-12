from os.path import join

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, FormView, UpdateView, DeleteView, ListView, TemplateView

from bookworm import settings
from bookworm.bookstore.forms import ReviewForm, BookCreateForm
from bookworm.bookstore.models import Book, Wishlist
from bookworm.core.clean_up import clean_up_files
from bookworm.core.mixins import StaffOnlyTestMixin
from bookworm.core.views import CategoriesNavMixin


class BookDetailView(CategoriesNavMixin, DetailView):
	model = Book
	template_name = 'shop/single-book.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['review_form'] = ReviewForm()
		return context


class BookCreateView(CategoriesNavMixin, StaffOnlyTestMixin, CreateView):
	model = Book
	form_class = BookCreateForm
	template_name = 'shop/create-book.html'

	def get_success_url(self):
		return reverse_lazy('book detail', kwargs={'pk': self.object.id})


class BookUpdateView(CategoriesNavMixin, StaffOnlyTestMixin, UpdateView):
	model = Book
	template_name = 'update-book.html'
	fields = ('title',
			  'author',
			  'price',
			  'cover_image',
			  'back_cover_image',
			  'category',
			  'short_description',
			  'long_description',
			  'format',
			  'pages',
			  'dimensions',
			  'publication_date',
			  'publisher',
			  'language',
			  )

	def get_success_url(self):
		return reverse_lazy('book detail', kwargs={'pk': self.object.id})


class BookDeleteView(CategoriesNavMixin, StaffOnlyTestMixin, DeleteView):
	model = Book
	template_name = 'delete-book.html'
	success_url = reverse_lazy('authors list')


class ReviewBookView(CategoriesNavMixin, LoginRequiredMixin, FormView):
	form_class = ReviewForm
	template_name = 'shop/single-book.html'

	def form_valid(self, form):
		book_id = self.request.headers['Referer'].split('/')[-2]
		book = Book.objects.get(pk=book_id)
		review = form.save(commit=False)
		review.user = self.request.user
		review.book = book
		review.save()
		self.set_ave_rating(book)
		return redirect('book detail', book_id)

	@staticmethod
	def set_ave_rating(obj):
		count = obj.review_set.count()
		if not count:
			return
		total = sum(r['rating'] for r in obj.review_set.values())
		ave_rating = round(total / count, 1)
		obj.ave_rating = ave_rating
		obj.save()


class BookListView(CategoriesNavMixin, TemplateView):
	template_name = 'shop/all-products-v6.html'

	def get_context_data(self, **kwargs):
		book_list = Book.objects.filter(category=self.kwargs['pk'])
		context = super().get_context_data(**kwargs)
		context['book_list'] = book_list
		return context


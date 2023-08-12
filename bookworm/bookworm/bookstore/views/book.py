from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, FormView

from bookworm.bookstore.forms import ReviewForm
from bookworm.bookstore.models import Book, Wishlist
from bookworm.core.mixins import StaffOnlyTestMixin


class BookDetailView(DetailView):
	model = Book
	template_name = 'shop/single-book.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['review_form'] = ReviewForm()
		return context


class BookCreateView(StaffOnlyTestMixin, CreateView):
	model = Book
	fields = ('title',
			  'author'
			  'price',
			  'cover_image',
			  'back_cover_image',
			  'category',
			  'short_description',
			  'long_description',
			  'format',
			  'pages',
			  'dimensions,'
			  'publication_date',
			  'publisher',
			  'language'
			  )

	template_name = 'shop/create-book.html'

	def get_success_url(self):
		return reverse_lazy('book detail', kwargs={'pk': self.object.id})


class AddToWishlistView(LoginRequiredMixin, View):

	def get(self, request, pk):
		book = Book.objects.get(pk=pk)
		wishlist_object = book.wishlist_set.filter(user_id=request.user.id).first()
		if not wishlist_object:
			Wishlist(
				book=book,
				user=request.user,
			).save()
		return redirect('book detail', pk)


class ReviewBookView(LoginRequiredMixin, FormView):
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

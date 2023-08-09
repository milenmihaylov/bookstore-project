from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import DetailView, CreateView, FormView

from bookworm.bookstore.forms import ReviewForm
from bookworm.bookstore.models import Book, Wishlist


class BookDetailView(DetailView):
	model = Book
	template_name = 'shop/single-book.html'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['ave_rating'] = self.object.review_set
		context['review_form'] = ReviewForm()
		return context


class BookCreateView(CreateView):
	model = Book
	fields = '__all__'
	template_name = 'shop/create-book.html'

	def get_success_url(self):
		return reverse_lazy('book detail', kwargs={'pk': self.object.id})


class AddToWishlistView(View):

	def get(self, request, pk):
		book = Book.objects.get(pk=pk)
		wishlist_object = book.wishlist_set.filter(user_id=request.user.id).first()
		if wishlist_object:
			wishlist_object.delete()
		else:
			Wishlist(
				book=book,
				user=request.user,
			).save()
		return redirect('book detail', pk)


class ReviewBookView(FormView):
	form_class = ReviewForm

	def form_valid(self, form):
		review = form.save(commit=False)
		review.user = self.request.user
		review.book = Book.objects.get(pk=self.kwargs['pk'])
		review.save()
		return redirect('book detail', self.kwargs['pk'])


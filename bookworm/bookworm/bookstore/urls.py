from django.urls import path

from bookworm.bookstore.views.author import AuthorCreateView, AuthorUpdateView, AuthorDeleteView, AuthorDetailView, \
	AuthorsListView
from bookworm.bookstore.views.book import BookDetailView, BookCreateView, AddToWishlistView, ReviewBookView
from bookworm.bookstore.views.category import CategoryCreateView, CategoryUpdateView, CategoryDeleteView, \
	CategoryListView
from bookworm.bookstore.views.index import IndexView

urlpatterns = [
	path('', IndexView.as_view(), name='index'),

	path('create-author/', AuthorCreateView.as_view(), name='create author'),
	path('update-author/<int:pk>', AuthorUpdateView.as_view(), name='update author'),
	path('delete-author/<int:pk>', AuthorDeleteView.as_view(), name='delete author'),
	path('author/<int:pk>/', AuthorDetailView.as_view(), name='author detail'),
	path('authors/', AuthorsListView.as_view(), name='authors list'),

	path('all-categories/', CategoryListView.as_view(), name='all categories'),
	path('create-category/', CategoryCreateView.as_view(), name='create category'),
	path('update-category/<int:pk>/', CategoryUpdateView.as_view(), name='update category'),
	path('delete-category/<int:pk>/', CategoryDeleteView.as_view(), name='delete category'),

	path('book/<int:pk>/', BookDetailView.as_view(), name='book detail'),
	path('create-book/', BookCreateView.as_view(), name='create book'),

	path('add-to-wishlist/<int:pk>', AddToWishlistView.as_view(), name='add to wishlist'),
	path('submit-review/', ReviewBookView.as_view(), name='submit review'),
]

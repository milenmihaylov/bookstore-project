from django.urls import path

from bookworm.bookstore.views.author import AuthorCreateView, AuthorUpdateView, AuthorDeleteView, AuthorDetailView, \
	AuthorsListView
from bookworm.bookstore.views.book import BookDetailView, BookCreateView, ReviewBookView, \
	BookUpdateView, BookDeleteView, BookListView, book_search, BookSearch
from bookworm.bookstore.views.category import CategoryCreateView, CategoryUpdateView, CategoryDeleteView, \
	CategoryListView
from bookworm.bookstore.views.index import IndexView, NewsletterSubscribeFormView, AboutUsView, TermsAndConditionsView, \
	ContactView, FAQView

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
	path('books/<int:pk>/', BookListView.as_view(), name='list books'),
	path('create-book/', BookCreateView.as_view(), name='create book'),
	path('update-book/<int:pk>/', BookUpdateView.as_view(), name='update book'),
	path('delete-book/<int:pk>/', BookDeleteView.as_view(), name='delete book'),

	path('submit-review/', ReviewBookView.as_view(), name='submit review'),
	path('search/', BookSearch.as_view(), name='search'),

	path('newsletter-subscribe/', NewsletterSubscribeFormView.as_view(), name='newsletter subscribe'),

	path('about-us/', AboutUsView.as_view(), name='about us'),
	path('terms-and-conditions/', TermsAndConditionsView.as_view(), name='terms'),
	path('contact/', ContactView.as_view(), name='contact'),
	path('faq/', FAQView.as_view(), name='faq'),
]

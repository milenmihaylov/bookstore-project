from django.urls import path

from bookworm.blog.views import BlogListView, ArticleDetailView, ArticleCreateView, ArticleUpdateView, ArticleDeleteView

urlpatterns = [
	path('', BlogListView.as_view(), name='blog'),
	path('article/<int:pk>/', ArticleDetailView.as_view(), name='article'),
	path('create-article/', ArticleCreateView.as_view(), name='create article'),
	path('update-article/<int:pk>/', ArticleUpdateView.as_view(), name='update article'),
	path('delete-article/<int:pk>', ArticleDeleteView.as_view(), name='delete article'),
]

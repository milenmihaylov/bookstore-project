from django.contrib import admin

from bookworm.bookstore.models import Book, Author, Category, Review, NewsletterList


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
	readonly_fields = ['ave_rating']
	list_display = ['title', 'author', 'price', 'category', 'format', 'pages',
					'publication_date', 'publisher', 'language', 'ave_rating'
					]
	list_filter = ['price', 'category', 'format', 'pages',
				   'publisher', 'language', 'ave_rating'
				   ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
	pass


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
	pass


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
	pass


@admin.register(NewsletterList)
class NewsletterAdmin(admin.ModelAdmin):
	pass

from bookworm.bookstore.models import Category


class CategoriesNavMixin:

	def get_context_data(self, **kwargs):
		context = super().get_context_data()
		context['categories'] = Category.objects.all()
		return context

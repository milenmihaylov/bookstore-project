from django.views.generic import TemplateView

from bookworm.core.views import CategoriesNavMixin


class IndexView(CategoriesNavMixin, TemplateView):
	template_name = 'home/index.html'

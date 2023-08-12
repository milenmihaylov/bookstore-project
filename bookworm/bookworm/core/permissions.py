from django.contrib.auth.mixins import PermissionRequiredMixin


class StaffOnlyPermission(PermissionRequiredMixin):
	permission_required = ('blog.add_article', 'bookstore.add_author')

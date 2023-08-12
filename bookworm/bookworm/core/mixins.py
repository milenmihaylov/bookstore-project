from django.contrib.auth.mixins import UserPassesTestMixin


class StaffOnlyTestMixin(UserPassesTestMixin):

	def test_func(self):
		return self.request.user.groups.filter(name='Staff').exists()

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from bookworm.bookworm_auth.models import BookwormUser


@admin.register(BookwormUser)
class BookwormUserAdmin(UserAdmin):
	fieldsets = (
		(None, {'fields': ('email', 'password')}),
		('Permissions', {
			'fields': ('is_staff', 'is_superuser', 'groups', 'user_permissions'),
		}),
		('Important dates', {'fields': ('last_login', 'date_joined')}),
	)
	add_fieldsets = (
		(None, {
			'classes': ('wide',),
			'fields': ('email', 'password1', 'password2'),
		}),
	)
	list_display = ('email', 'is_staff')
	list_filter = ('is_staff', 'is_superuser', 'groups')
	search_fields = ('email',)
	ordering = ('email',)
	filter_horizontal = ('groups', 'user_permissions',)
	readonly_fields = ('email', 'last_login', 'date_joined')

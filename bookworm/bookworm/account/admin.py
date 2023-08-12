from django.contrib import admin

from bookworm.account.models import Account


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
	pass

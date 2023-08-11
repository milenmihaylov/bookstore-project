from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

from bookworm.account.models import Account
from bookworm.bookworm_auth.models import BookwormUser

USER_MODEL = get_user_model()


@receiver(post_save, sender=BookwormUser)
def create_user_account(sender, instance, created, **kwargs):
	if created:
		Account.objects.create(
			user=instance
		)

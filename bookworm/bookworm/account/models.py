from django.contrib.auth import get_user_model
from django.db import models


USER_MODEL = get_user_model()


class Account(models.Model):
	user = models.OneToOneField(
		to=USER_MODEL,
		primary_key=True,
		on_delete=models.CASCADE,
	)

	first_name = models.CharField(
		max_length=20,
		blank=True,
	)

	last_name = models.CharField(
		max_length=20,
		blank=True,
	)

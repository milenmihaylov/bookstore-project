from django.contrib.auth import get_user_model
from django.db import models

from bookworm.bookstore.models import Book

UserModel = get_user_model()


class CartItem(models.Model):
	user = models.ForeignKey(
		UserModel,
		on_delete=models.CASCADE
	)
	book = models.ForeignKey(
		Book,
		on_delete=models.CASCADE
	)
	quantity = models.PositiveIntegerField(
		default=1,
	)

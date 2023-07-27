from _decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


USER_MODEL = get_user_model()


class Author(models.Model):
	name = models.CharField(
		max_length=30,
	)
	image = models.ImageField(
		upload_to='images/authors',
	)
	about = models.TextField()


class Category(models.Model):
	category = models.CharField(
		max_length=30,
	)


class Book(models.Model):
	title = models.CharField(
		max_length=50,
	)
	author = models.ForeignKey(
		to=Author,
		on_delete=models.SET_NULL,
		null=True,
	)
	price = models.DecimalField(
		max_digits=7,
		decimal_places=2,
		validators=[
			MinValueValidator(Decimal(0.00)),
		],
	)
	cover_image = models.ImageField(
		upload_to='images/book-covers',
	)
	back_cover_image = models.ImageField(
		upload_to='images/book-covers',
		blank=True,
		null=True,
	)
	category = models.ForeignKey(
		to=Category,
		on_delete=models.SET_NULL,
		null=True,
	)
	description = models.TextField()


class Review(models.Model):
	book = models.ForeignKey(
		to=Book,
		on_delete=models.CASCADE,
	)
	user = models.ForeignKey(
		to=USER_MODEL,
		on_delete=models.CASCADE,
	)
	stars = models.PositiveSmallIntegerField(
		validators=[
			MaxValueValidator(5),
		],
	)
	title = models.CharField(
		max_length=50,
	)
	text = models.TextField(
		blank=True,
		null=True,
	)

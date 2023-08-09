from datetime import date
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

	def __str__(self):
		return self.name


class Category(models.Model):
	category = models.CharField(
		max_length=30,
	)

	def __str__(self):
		return self.category


class Book(models.Model):
	FORMAT_CHOICE_PAPERBACK = 'paperback'
	FORMAT_CHOICE_HARDCOVER = 'hardcover'
	FORMAT_CHOICE_KINDLE = 'kindle'

	FORMAT_CHOICES = (
		(FORMAT_CHOICE_PAPERBACK, 'Paperback'),
		(FORMAT_CHOICE_HARDCOVER, 'Hardcover'),
		(FORMAT_CHOICE_KINDLE, 'Kindle'),
	)

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
	short_description = models.TextField(
		default='',
	)
	long_description = models.TextField(
		default='',
	)
	format = models.CharField(
		max_length=10,
		choices=FORMAT_CHOICES,
	)
	pages = models.PositiveIntegerField()
	dimensions = models.CharField(
		max_length=30,
		default=''
	)
	publication_date = models.DateField(
		blank=True,
		default=date.today
	)
	publisher = models.CharField(
		max_length=30,
		default='',
	)
	language = models.CharField(
		max_length=30,
		default='',
	)


class Review(models.Model):
	book = models.ForeignKey(
		to=Book,
		on_delete=models.CASCADE,
	)
	user = models.ForeignKey(
		to=USER_MODEL,
		on_delete=models.CASCADE,
	)
	rating = models.PositiveIntegerField(
		choices=[(i, i) for i in range(1, 6)],
	)
	title = models.CharField(
		max_length=50,
	)
	text = models.TextField(
		blank=True,
		null=True,
	)
	created_at = models.DateField(
		auto_now_add=True,
	)


class Wishlist(models.Model):
	book = models.ForeignKey(
		to=Book,
		on_delete=models.CASCADE,
	)
	user = models.ForeignKey(
		to=USER_MODEL,
		on_delete=models.CASCADE,
		null=True,
	)


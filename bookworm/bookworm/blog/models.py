from datetime import date

from django.db import models


class Article(models.Model):
	writer = models.CharField(
		max_length=30,
	)
	title = models.CharField(
		max_length=100,
	)
	text = models.TextField()
	image = models.ImageField(
		upload_to='images/blog',
	)
	date = models.DateField(
		auto_now_add=True,
		blank=True,
	)

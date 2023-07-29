from django.db import models


class Article(models.Model):
	writer = models.CharField(
		max_length=30,
	)
	text = models.TextField()
	image = models.ImageField(
		upload_to='images/blog',
	)

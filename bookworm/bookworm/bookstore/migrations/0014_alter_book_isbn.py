# Generated by Django 4.2.3 on 2023-08-12 14:57

import bookworm.bookstore.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0013_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='isbn',
            field=models.CharField(null=True, validators=[bookworm.bookstore.validators.validate_isbn_length]),
        ),
    ]

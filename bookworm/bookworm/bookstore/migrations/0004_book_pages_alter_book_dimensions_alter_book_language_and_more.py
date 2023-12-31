# Generated by Django 4.2.3 on 2023-08-07 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0003_remove_book_description_book_dimensions_book_format_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='dimensions',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='language',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='long_description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AlterField(
            model_name='book',
            name='short_description',
            field=models.TextField(default=''),
        ),
    ]

# Generated by Django 4.2.3 on 2023-08-07 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0006_review_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='date',
            new_name='created_at',
        ),
        migrations.RemoveField(
            model_name='review',
            name='stars',
        ),
        migrations.AddField(
            model_name='review',
            name='rating',
            field=models.PositiveIntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=5),
            preserve_default=False,
        ),
    ]

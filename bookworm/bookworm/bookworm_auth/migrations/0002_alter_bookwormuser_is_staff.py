# Generated by Django 4.2.3 on 2023-08-10 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookworm_auth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookwormuser',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.'),
        ),
    ]

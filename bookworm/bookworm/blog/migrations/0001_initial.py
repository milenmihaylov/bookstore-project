# Generated by Django 4.2.3 on 2023-07-29 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('writer', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='images/blog')),
            ],
        ),
    ]

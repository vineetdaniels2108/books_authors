# Generated by Django 3.1.7 on 2021-03-11 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books_author_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='Love is in the air'),
        ),
    ]
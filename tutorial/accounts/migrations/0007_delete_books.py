# Generated by Django 2.2 on 2019-04-23 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_books_categoryname'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Books',
        ),
    ]
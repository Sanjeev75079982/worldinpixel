# Generated by Django 3.0.5 on 2020-06-23 11:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_image_favourite'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
    ]
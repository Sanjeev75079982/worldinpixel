# Generated by Django 3.0.5 on 2020-06-22 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_auto_20200622_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='subscription',
            name='sub_type',
            field=models.CharField(max_length=50, null=True),
        ),
    ]

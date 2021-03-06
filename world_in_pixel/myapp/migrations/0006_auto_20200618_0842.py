# Generated by Django 3.0.5 on 2020-06-18 08:42

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('myapp', '0005_pricing_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Subscription_status', models.BooleanField()),
                ('pro_created', models.DateTimeField(default=datetime.datetime(2020, 6, 18, 8, 42, 54, 271658, tzinfo=utc))),
                ('approved_user', models.BooleanField()),
                ('price', models.IntegerField()),
                ('pro_user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Pricing',
        ),
    ]

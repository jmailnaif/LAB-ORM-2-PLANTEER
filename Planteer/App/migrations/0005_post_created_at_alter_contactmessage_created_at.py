# Generated by Django 5.0.3 on 2024-03-25 07:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0004_contactmessage_alter_post_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 25, 10, 35, 6, 415582)),
        ),
        migrations.AlterField(
            model_name='contactmessage',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 25, 10, 35, 6, 415582)),
        ),
    ]
# Generated by Django 5.0.3 on 2024-03-21 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='eidble',
            field=models.BooleanField(default=True),
        ),
    ]
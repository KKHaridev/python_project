# Generated by Django 3.2.3 on 2021-05-22 06:47

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='desc',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]

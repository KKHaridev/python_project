# Generated by Django 3.2.3 on 2021-05-22 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('event', models.CharField(max_length=100)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('deadline', models.DateTimeField()),
            ],
        ),
    ]
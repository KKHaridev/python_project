# Generated by Django 3.2.3 on 2021-05-22 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_events_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mainbanner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('eventName', models.CharField(max_length=100)),
                ('eventdesc', models.TextField()),
            ],
        ),
        migrations.RenameField(
            model_name='events',
            old_name='link',
            new_name='gform_link',
        ),
    ]

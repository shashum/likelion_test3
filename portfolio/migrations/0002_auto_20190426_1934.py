# Generated by Django 2.1.7 on 2019-04-26 10:34

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='created_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='person',
            name='published_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]

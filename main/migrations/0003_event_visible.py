# Generated by Django 3.0.5 on 2020-05-15 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20200515_2003'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='visible',
            field=models.BooleanField(default=1),
        ),
    ]

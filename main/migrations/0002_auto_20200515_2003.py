# Generated by Django 3.0.5 on 2020-05-15 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.CharField(max_length=120),
        ),
    ]
# Generated by Django 3.0.5 on 2020-05-23 18:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20200523_1951'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='event',
            name='emoji_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]

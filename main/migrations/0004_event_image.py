# Generated by Django 3.0.5 on 2020-05-16 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_event_visible'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
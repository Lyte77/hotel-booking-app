# Generated by Django 5.1.1 on 2024-10-23 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0005_hotel_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='background_image',
            field=models.URLField(blank=True, null=True),
        ),
    ]

# Generated by Django 5.1.1 on 2024-10-23 14:51

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0006_hotel_background_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='features',
        ),
        migrations.AddField(
            model_name='hotel',
            name='activities',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Spa', 'Spa'), ('Gym', 'Gym'), ('Car park', 'Car park'), ('Kids Play Area', 'Kids Play Area')], max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='payment_method',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Cash', 'Cash'), ('Crypto', 'Crypto')], max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='services',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Dry cleaning', 'Dry cleaning'), ('Wifi', 'Wifi'), ('Room service', 'Room service'), ('Special service', 'Special service'), ('Waiting area', 'waiting area'), ('Secrete smoking area', 'Secrete smoking area'), ('Lift', 'Lift')], max_length=200),
        ),
        migrations.AddField(
            model_name='hotel',
            name='staff_languages',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('English', 'English'), ('French', 'French'), ('German', 'German'), ('Portuguese', 'Portuguese')], max_length=200),
        ),
    ]

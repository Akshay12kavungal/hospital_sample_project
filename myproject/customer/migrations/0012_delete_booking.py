# Generated by Django 5.0.4 on 2024-05-09 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0011_alter_profile_profile_pic'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Booking',
        ),
    ]
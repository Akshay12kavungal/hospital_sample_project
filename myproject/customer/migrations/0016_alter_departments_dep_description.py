# Generated by Django 5.0.6 on 2024-05-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0015_delete_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departments',
            name='dep_description',
            field=models.CharField(max_length=100),
        ),
    ]

# Generated by Django 5.0.7 on 2025-01-08 08:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0006_announcement'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registration',
            name='Telefon_raqamingiz',
            field=models.IntegerField(),
        ),
    ]

# Generated by Django 5.0.7 on 2025-01-07 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0005_rename_name_registration_ism_familyangiz_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('is_active', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]

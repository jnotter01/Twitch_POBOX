# Generated by Django 5.1.7 on 2025-03-10 03:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fanmail', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fanmail',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='fanmail_images/'),
        ),
    ]

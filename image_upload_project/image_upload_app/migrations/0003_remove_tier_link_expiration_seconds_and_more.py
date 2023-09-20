# Generated by Django 4.2.5 on 2023-09-19 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('image_upload_app', '0002_remove_image_thumbnail_200_link_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tier',
            name='link_expiration_seconds',
        ),
        migrations.AddField(
            model_name='image',
            name='link_expiration_seconds',
            field=models.IntegerField(default=3600),
        ),
    ]

# Generated by Django 5.0 on 2023-12-16 04:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('video_management', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='file_content',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]

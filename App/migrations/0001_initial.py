# Generated by Django 4.2.3 on 2023-07-30 17:54

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('alt_text', models.CharField(max_length=100)),
                ('background_image', models.ImageField(upload_to='banner_images/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['jpg', 'jpeg', 'png'])])),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('banner_title', models.CharField(max_length=100)),
                ('total_students', models.IntegerField(default=0)),
                ('total_teachers', models.IntegerField(default=0)),
                ('total_classes', models.IntegerField(default=0)),
                ('upcoming_events', models.TextField(blank=True)),
                ('notifications', models.TextField(blank=True)),
                ('add_date', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='GalleryItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='gallery/photos/')),
                ('video', models.FileField(blank=True, null=True, upload_to='gallery/videos/')),
            ],
        ),
        migrations.CreateModel(
            name='Home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
            ],
        ),
    ]
# Generated by Django 4.2.3 on 2023-07-30 19:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='background_image',
            new_name='image',
        ),
    ]
# Generated by Django 4.2.7 on 2023-11-20 01:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banner',
            old_name='banner',
            new_name='Image',
        ),
        migrations.RenameField(
            model_name='slider',
            old_name='slider',
            new_name='Image',
        ),
    ]

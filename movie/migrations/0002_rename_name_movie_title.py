# Generated by Django 4.0.3 on 2022-04-08 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='name',
            new_name='title',
        ),
    ]
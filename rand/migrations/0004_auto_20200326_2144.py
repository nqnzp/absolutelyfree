# Generated by Django 3.0.4 on 2020-03-27 01:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rand', '0003_album'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='created_at',
            new_name='pub_date',
        ),
        migrations.RenameField(
            model_name='bandname',
            old_name='created_at',
            new_name='pub_date',
        ),
    ]
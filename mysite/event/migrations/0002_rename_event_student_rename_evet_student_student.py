# Generated by Django 5.0.3 on 2024-04-03 09:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='event',
            new_name='Student',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='evet',
            new_name='Student',
        ),
    ]

# Generated by Django 5.1.3 on 2024-12-06 01:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='board',
            old_name='bcondent',
            new_name='bcontent',
        ),
    ]

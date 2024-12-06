# Generated by Django 5.1.3 on 2024-12-06 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('pw', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('nicName', models.CharField(max_length=100)),
                ('phone', models.CharField(default='010-0000-0000', max_length=20)),
                ('gender', models.CharField(default='남자', max_length=10)),
                ('hobby', models.CharField(default='game', max_length=100)),
                ('mdate', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]

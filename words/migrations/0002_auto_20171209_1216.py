# Generated by Django 2.0 on 2017-12-09 12:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('words', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='word',
            options={'ordering': ['-count']},
        ),
    ]

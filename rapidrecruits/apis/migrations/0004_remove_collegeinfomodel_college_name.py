# Generated by Django 3.1.2 on 2022-08-09 13:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0003_auto_20220809_1845'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='collegeinfomodel',
            name='college_name',
        ),
    ]

# Generated by Django 3.2 on 2021-05-04 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sistema', '0003_auto_20210504_1525'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='instrutor',
            name='data_nascimento',
        ),
    ]

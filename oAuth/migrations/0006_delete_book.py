# Generated by Django 3.2.21 on 2023-09-18 06:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('oAuth', '0005_alter_newuser_code'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Book',
        ),
    ]
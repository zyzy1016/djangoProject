# Generated by Django 3.2.21 on 2023-09-12 05:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('oAuth', '0004_newuser_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newuser',
            name='code',
            field=models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='uuid'),
        ),
    ]
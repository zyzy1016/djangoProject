# Generated by Django 3.2.21 on 2023-09-11 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('oAuth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='书名')),
                ('author', models.CharField(max_length=10, verbose_name='作者')),
            ],
        ),
    ]
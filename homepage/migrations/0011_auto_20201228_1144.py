# Generated by Django 3.1 on 2020-12-28 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0010_admin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='roles',
            field=models.CharField(max_length=255),
        ),
    ]

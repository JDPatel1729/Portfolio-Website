# Generated by Django 3.1 on 2020-12-27 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20201226_0935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='name',
            new_name='proj_name',
        ),
    ]

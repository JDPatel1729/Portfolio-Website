# Generated by Django 3.1 on 2020-12-28 03:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0007_auto_20201227_1640'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proj_category',
            field=models.CharField(choices=[('all', 'all'), ('app', 'app'), ('web', 'web')], default='all', max_length=10),
        ),
    ]

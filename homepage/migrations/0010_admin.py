# Generated by Django 3.1 on 2020-12-28 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0009_auto_20201228_0945'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=15)),
                ('lname', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=13)),
                ('website', models.URLField()),
                ('location', models.CharField(max_length=20)),
                ('twitter', models.URLField()),
                ('insta', models.URLField()),
                ('github', models.URLField()),
                ('linkedIn', models.URLField()),
                ('roles', models.JSONField()),
            ],
        ),
    ]

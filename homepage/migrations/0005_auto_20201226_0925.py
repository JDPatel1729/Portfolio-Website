# Generated by Django 3.1 on 2020-12-26 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_auto_20201224_1549'),
    ]

    operations = [
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=20)),
                ('skill_val', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='NavigationTab',
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]

# Generated by Django 3.1.2 on 2020-11-17 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0007_resultgame'),
    ]

    operations = [
        migrations.AddField(
            model_name='regulargame',
            name='score',
            field=models.CharField(default='-', max_length=7),
        ),
    ]
# Generated by Django 3.1.2 on 2020-11-18 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0009_auto_20201117_1906'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resultgame',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

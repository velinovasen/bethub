# Generated by Django 3.1.2 on 2020-11-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('traffic', '0008_regulargame_score'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regulargame',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]

# Generated by Django 4.2 on 2023-04-19 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_alter_data_avg_alter_data_max_alter_data_min'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='avg',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='data',
            name='max',
            field=models.FloatField(),
        ),
    ]

# Generated by Django 4.0.6 on 2022-08-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('devansh', '0002_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='prorate',
            field=models.IntegerField(),
        ),
    ]

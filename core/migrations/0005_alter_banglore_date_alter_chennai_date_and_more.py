# Generated by Django 4.1 on 2022-11-14 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_chennai_mumbai'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banglore',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='chennai',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='mumbai',
            name='date',
            field=models.DateField(),
        ),
    ]

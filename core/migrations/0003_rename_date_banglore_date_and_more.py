# Generated by Django 4.1 on 2022-11-14 09:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_banglore'),
    ]

    operations = [
        migrations.RenameField(
            model_name='banglore',
            old_name='Date',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='banglore',
            old_name='Line1',
            new_name='line1',
        ),
        migrations.RenameField(
            model_name='banglore',
            old_name='Line2',
            new_name='line2',
        ),
        migrations.RenameField(
            model_name='banglore',
            old_name='Line3',
            new_name='line3',
        ),
        migrations.RenameField(
            model_name='banglore',
            old_name='Line4',
            new_name='line4',
        ),
        migrations.RenameField(
            model_name='banglore',
            old_name='Line5',
            new_name='line5',
        ),
    ]

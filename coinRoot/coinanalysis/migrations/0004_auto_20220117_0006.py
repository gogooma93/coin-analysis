# Generated by Django 3.2.5 on 2022-01-17 00:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coinanalysis', '0003_alter_bitcoiner_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bitcoiner',
            name='close',
        ),
        migrations.RemoveField(
            model_name='bitcoiner',
            name='high',
        ),
        migrations.RemoveField(
            model_name='bitcoiner',
            name='low',
        ),
        migrations.RemoveField(
            model_name='bitcoiner',
            name='open',
        ),
        migrations.RemoveField(
            model_name='bitcoiner',
            name='value',
        ),
        migrations.RemoveField(
            model_name='bitcoiner',
            name='volume',
        ),
        migrations.RemoveField(
            model_name='bitcoiner',
            name='won',
        ),
    ]

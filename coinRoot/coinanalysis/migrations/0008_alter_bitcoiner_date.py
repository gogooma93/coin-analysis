# Generated by Django 3.2.5 on 2022-01-17 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coinanalysis', '0007_alter_bitcoiner_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bitcoiner',
            name='date',
            field=models.CharField(max_length=100),
        ),
    ]

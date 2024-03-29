# Generated by Django 3.2.5 on 2022-01-15 13:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BitcoinER',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.TextField(max_length=100)),
                ('open', models.IntegerField(max_length=100)),
                ('high', models.IntegerField(max_length=100)),
                ('low', models.IntegerField(max_length=100)),
                ('close', models.IntegerField(max_length=100)),
                ('volume', models.IntegerField(max_length=100)),
                ('value', models.IntegerField(max_length=100)),
                ('won', models.FloatField(max_length=100)),
            ],
        ),
    ]

# Generated by Django 4.2.7 on 2023-11-09 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('smolApi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='csvfile',
            name='name',
            field=models.CharField(default='default.csv', max_length=150),
        ),
    ]

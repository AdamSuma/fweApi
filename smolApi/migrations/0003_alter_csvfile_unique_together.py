# Generated by Django 4.2.7 on 2023-11-09 15:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('smolApi', '0002_csvfile_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='csvfile',
            unique_together={('uploaded_at', 'name')},
        ),
    ]

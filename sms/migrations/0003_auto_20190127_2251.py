# Generated by Django 2.1.5 on 2019-01-27 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20190127_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='roll_number',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]

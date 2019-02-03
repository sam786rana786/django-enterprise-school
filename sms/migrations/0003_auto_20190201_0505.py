# Generated by Django 2.1.5 on 2019-02-01 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_auto_20190128_2340'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='class',
            options={'verbose_name_plural': 'classes'},
        ),
        migrations.AddField(
            model_name='attendance',
            name='is_late',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='is_late_for',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='attendance',
            name='is_present',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(),
        ),
    ]
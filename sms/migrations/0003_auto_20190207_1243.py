# Generated by Django 2.1.5 on 2019-02-07 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sms', '0002_expense_amount'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feetype',
            name='section',
        ),
        migrations.AddField(
            model_name='feetype',
            name='for_class',
            field=models.ManyToManyField(to='sms.Class'),
        ),
    ]

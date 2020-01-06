# Generated by Django 2.2.9 on 2020-01-06 18:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PromotionCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=50)),
                ('minimum_avg', models.FloatField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='SectionPromotionCriteria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('promotion_criteria', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='promotion.PromotionCriteria')),
                ('section', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sms.Section')),
            ],
        ),
    ]
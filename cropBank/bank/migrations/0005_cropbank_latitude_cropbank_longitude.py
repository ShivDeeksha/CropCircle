# Generated by Django 5.0.1 on 2024-01-29 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0004_cropbank_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropbank',
            name='latitude',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='cropbank',
            name='longitude',
            field=models.FloatField(blank=True, null=True),
        ),
    ]

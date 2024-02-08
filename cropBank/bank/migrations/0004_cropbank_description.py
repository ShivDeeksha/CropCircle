# Generated by Django 5.0.1 on 2024-01-29 03:45

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0003_cropbank_bank_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='cropbank',
            name='description',
            field=models.CharField(default=django.utils.timezone.now, max_length=1000),
            preserve_default=False,
        ),
    ]

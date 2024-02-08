# Generated by Django 5.0.1 on 2024-01-27 12:49

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cropbank',
            name='bank_image',
        ),
        migrations.AddField(
            model_name='cropbank',
            name='review',
            field=models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True),
        ),
        migrations.CreateModel(
            name='BankCommodity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('crop_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commodities', to='bank.cropbank')),
            ],
        ),
        migrations.CreateModel(
            name='BankImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='crop_bank_images/')),
                ('crop_bank', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='bank.cropbank')),
            ],
        ),
    ]

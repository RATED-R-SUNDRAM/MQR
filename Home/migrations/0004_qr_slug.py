# Generated by Django 4.0.2 on 2022-02-27 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_qr'),
    ]

    operations = [
        migrations.AddField(
            model_name='qr',
            name='slug',
            field=models.CharField(blank=True, max_length=1000),
        ),
    ]
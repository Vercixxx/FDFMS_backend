# Generated by Django 5.0.1 on 2024-02-26 14:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0006_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='driver',
            name='rate',
            field=models.ForeignKey(blank=True, db_column='rate', null=True, on_delete=django.db.models.deletion.SET_NULL, to='driver.rating'),
        ),
    ]

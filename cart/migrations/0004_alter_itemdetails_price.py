# Generated by Django 3.2.5 on 2021-07-17 19:25

import cart.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0003_alter_myorder_distance'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemdetails',
            name='price',
            field=models.FloatField(validators=[cart.models.priceLimit]),
        ),
    ]
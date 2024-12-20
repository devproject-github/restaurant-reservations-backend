# Generated by Django 5.1.1 on 2024-10-27 17:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0002_alter_customer_options_alter_customer_managers_and_more'),
        ('reservations', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='customer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to='customers.customer'),
        ),
        migrations.AlterField(
            model_name='rating',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ratings', to='customers.customer'),
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
    ]

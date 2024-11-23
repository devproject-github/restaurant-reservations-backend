# Generated by Django 5.1.1 on 2024-11-03 21:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0002_alter_reservation_customer_alter_rating_customer_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_date',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='area',
        ),
        migrations.RemoveField(
            model_name='reservation',
            name='reservation_turn',
        ),
        migrations.AlterField(
            model_name='reservation',
            name='number_guests',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Number of guests'),
        ),
        migrations.AlterField(
            model_name='table',
            name='area',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='tables', to='reservations.area'),
        ),
        migrations.AlterField(
            model_name='table',
            name='capacity',
            field=models.PositiveIntegerField(verbose_name='Capacity'),
        ),
        migrations.AlterField(
            model_name='table',
            name='status',
            field=models.CharField(choices=[('available', 'Available'), ('occupied', 'Occupied'), ('maintenance', 'Under Maintenance')], default='available', max_length=20, verbose_name='Status'),
        ),
        migrations.AlterField(
            model_name='table',
            name='table_number',
            field=models.IntegerField(unique=True, verbose_name='Table number'),
        ),
        migrations.CreateModel(
            name='TableSchedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Date')),
                ('is_available', models.BooleanField(default=True, verbose_name='Is Available')),
                ('table', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='schedules', to='reservations.table')),
                ('turn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservations.turn')),
            ],
            options={
                'verbose_name': 'Table schedule',
                'verbose_name_plural': 'Schedule of Tables',
                'db_table': 'reservations_table_schedule',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='reservation',
            name='table_schedule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='reservations.tableschedule'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='TableAvailability',
        ),
        migrations.AddConstraint(
            model_name='tableschedule',
            constraint=models.UniqueConstraint(fields=('table', 'date', 'turn'), name='unique_table_schedule'),
        ),
    ]
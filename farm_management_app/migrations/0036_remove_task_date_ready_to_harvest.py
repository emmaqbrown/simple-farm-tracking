# Generated by Django 4.2.3 on 2023-07-24 19:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('farm_management_app', '0035_remove_task_cultivar_task_actual_amount_harvested_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='date_ready_to_harvest',
        ),
    ]

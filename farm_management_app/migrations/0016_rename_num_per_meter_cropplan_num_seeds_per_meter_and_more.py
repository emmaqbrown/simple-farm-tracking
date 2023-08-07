# Generated by Django 4.2.3 on 2023-07-20 13:42

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('farm_management_app', '0015_alter_task_beds_alter_task_cultivars'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cropplan',
            old_name='num_per_meter',
            new_name='num_seeds_per_meter',
        ),
        migrations.RemoveField(
            model_name='cropplan',
            name='harvest_range_end_date',
        ),
        migrations.RemoveField(
            model_name='cropplan',
            name='harvest_range_start_date',
        ),
        migrations.AddField(
            model_name='cropplan',
            name='is_harvested',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cropplan',
            name='is_planted',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='cultivar',
            name='harvest_range_end_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cultivar',
            name='harvest_range_start_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cultivar',
            name='temperture_germination',
            field=models.DecimalField(decimal_places=2, default=10, max_digits=5),
            preserve_default=False,
        ),
    ]

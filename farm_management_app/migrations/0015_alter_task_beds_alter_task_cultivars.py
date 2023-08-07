# Generated by Django 4.2.3 on 2023-07-20 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_management_app', '0014_remove_task_bed_task_beds_remove_task_cultivars_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='beds',
            field=models.ManyToManyField(blank=True, to='farm_management_app.bed'),
        ),
        migrations.AlterField(
            model_name='task',
            name='cultivars',
            field=models.ManyToManyField(blank=True, to='farm_management_app.cultivar'),
        ),
    ]

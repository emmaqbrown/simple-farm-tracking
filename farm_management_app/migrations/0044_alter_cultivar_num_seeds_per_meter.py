# Generated by Django 4.2.3 on 2023-07-25 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_management_app', '0043_alter_species_temperture_germination'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cultivar',
            name='num_seeds_per_meter',
            field=models.PositiveSmallIntegerField(blank=True, null=True),
        ),
    ]

# Generated by Django 4.2.4 on 2023-10-17 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('farm_management_app', '0002_cropplan_num_rows_cultivar_num_rows_species_num_rows'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultivar',
            name='image_url',
            field=models.URLField(null=True),
        ),
    ]
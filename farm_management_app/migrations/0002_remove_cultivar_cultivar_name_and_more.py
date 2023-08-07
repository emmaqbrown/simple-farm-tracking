# Generated by Django 4.2.3 on 2023-07-20 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_management_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cultivar',
            name='cultivar_name',
        ),
        migrations.RemoveField(
            model_name='plantfamily',
            name='family_name',
        ),
        migrations.RemoveField(
            model_name='species',
            name='species_name',
        ),
        migrations.AddField(
            model_name='cultivar',
            name='name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='plantfamily',
            name='botanical_name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='species',
            name='botanical_name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AddField(
            model_name='species',
            name='common_name',
            field=models.CharField(default='', max_length=60),
        ),
        migrations.AlterField(
            model_name='cultivar',
            name='species',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='farm_management_app.species'),
        ),
    ]

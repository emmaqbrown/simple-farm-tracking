# Generated by Django 4.2.3 on 2023-07-20 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('farm_management_app', '0004_alter_cultivar_varietal_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('notes', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bed',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=60)),
                ('length_meters', models.DecimalField(decimal_places=2, max_digits=5)),
                ('width_meters', models.DecimalField(decimal_places=2, max_digits=5)),
                ('active', models.BooleanField(default=True)),
                ('area_square_meters', models.DecimalField(decimal_places=2, max_digits=8)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farm_management_app.area')),
            ],
        ),
    ]

from django.db import models
from .models_location import Bed
from django.utils.text import slugify

class PlantFamily(models.Model):
    botanical_name = models.CharField(max_length=60, default='')
    common_name = models.CharField(max_length=60, default='')

    slug = models.CharField(max_length=60, blank=True,default='')

    def __str__(self):
        return f"{self.botanical_name} | {self.common_name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.botanical_name)
        super(PlantFamily, self).save(*args, **kwargs)

class Species(models.Model):
    plant_family = models.ForeignKey(PlantFamily, on_delete=models.CASCADE)

    botanical_name = models.CharField(max_length=60, default='')
    alias_botanical_name = models.CharField(max_length=100, null=True, blank=True)
    common_name = models.CharField(max_length=60, default='')

    PLANT_TYPE_CHOICES = [
        ('A', 'annual'),
        ('B', 'biannual'),
        ('P', 'perennial'),
    ]
    
    plant_type = models.CharField(max_length=1, choices=PLANT_TYPE_CHOICES)

    plating_distance_cm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    sowing_depth_cm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    temperture_germination = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    slug = models.CharField(max_length=60, blank=True,default='')

    def __str__(self):
        return f"{self.botanical_name} - {self.common_name}"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.botanical_name)
        super(Species, self).save(*args, **kwargs)

class Cultivar(models.Model):
    species = models.ForeignKey(Species, on_delete=models.CASCADE, default='')

    name = models.CharField(max_length=60, default='')
    varietal_name = models.CharField(max_length=60, blank= True, default='')
    seed_supplier = models.CharField(max_length=60, blank= True)

    plating_distance_cm = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)

    sowing_depth_cm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    num_seeds_per_meter = models.PositiveSmallIntegerField(blank=True, null=True)


    days_seeding_to_transplatning = models.PositiveSmallIntegerField(blank=True, null=True)

    harvest_days_to_maturity_min = models.PositiveSmallIntegerField()
    harvest_days_to_maturity_max = models.PositiveSmallIntegerField()

    active = models.BooleanField(default=True)


    notes  = models.TextField(blank=True)

    slug = models.CharField(max_length=60, blank=True,default='')

    def __str__(self):
        return f"{self.species.common_name}, {self.name}"

    def save(self, *args, **kwargs):
        if self.plating_distance_cm == None:
            self.plating_distance_cm = self.species.plating_distance_cm

        if self.sowing_depth_cm == None:
            self.sowing_depth_cm = self.species.sowing_depth_cm

        self.slug = slugify(self.name)
        super(Cultivar, self).save(*args, **kwargs)

    def get_beds(self):
        beds = []
        for cropplan in self.cropplan_set.all().filter(is_harvested=False):
            for bed in cropplan.beds.all():
                if bed not in beds:
                    beds.append(bed)
        return beds





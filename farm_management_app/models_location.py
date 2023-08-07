from django.db import models
from django.utils.text import slugify
import datetime


class Location(models.Model):
    name = models.CharField(max_length=60, null=True)
    bed_length_meters = models.PositiveSmallIntegerField(blank=True, null=True)
    bed_width_centimeters = models.PositiveSmallIntegerField( blank=True, null=True)

    bed_area_meters_squared = models.PositiveSmallIntegerField(null=True, blank=True)

    notes  = models.TextField(blank=True)

    slug = models.CharField(max_length=60, blank=True,null=True)

    
    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)

        if self.bed_length_meters and self.bed_width_centimeters:
            self.bed_area_meters_squared = float(self.bed_length_meters) * float(self.bed_width_centimeters)*.01
        
        super(Location, self).save(*args, **kwargs)


class Bed(models.Model):
    name = models.CharField(max_length=60, null=True)

    location = models.ForeignKey(Location, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

    def get_current_upcoming_cropplans(self):

        cropplans = self.cropplan_set.all().filter(date_of_planting__gte=datetime.date.today())
        return cropplans

    def get_historical_cropplans(self):
        cropplans = self.cropplan_set.all().filter(date_of_planting__lt=datetime.date.today())
        return cropplans

    def get_curr_year_tasks(self):
        curr_year = datetime.date.today().year
        curr_year_start = datetime.date(curr_year, 1, 1)
        
        tasks = self.task_set.all().order_by('due_date').filter(due_date__gte=curr_year_start)
        return tasks

    def get_next_task(self):
        if self.cropplan_set.all().first():
            next_task = self.cropplan_set.all().first().task_set.all().latest('-due_date')
        else:
            return None






    


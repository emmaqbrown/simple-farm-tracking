from django.db import models
from .models_location import Bed, Location
from .models_crop_plan import CropPlan

# CHAGNE DATE TO EURPOEAN

class Task(models.Model):
    name = models.CharField(max_length=60, default='')
    due_date = models.DateField()

    TASK_TYPE_CHOICES = [
        ('D', 'direct seeding'), 
        ('P', 'pre-seeding'), 
        ('B', 'bed preparation'),
        ('T', 'transplant'),
        ('H', 'harvest'),
        ('T', 'terminate'),
        ('O', 'other'),
    ]

    task_type = models.CharField(max_length=1, choices=TASK_TYPE_CHOICES)

    location = models.ForeignKey(Location,on_delete=models.CASCADE, null=True, blank=True)
    beds =  models.ManyToManyField(Bed, blank=True)

    cropplan = models.ForeignKey(CropPlan, on_delete=models.CASCADE, null=True, blank=True)
    
    completed = models.BooleanField(default=False)
    auto_created = models.BooleanField(default=False)

    intended_amount_harvested = models.PositiveSmallIntegerField(null=True,blank=True)
    actual_amount_harvested = models.PositiveSmallIntegerField(null=True,blank=True)

    notes  = models.TextField(blank=True)


    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        # if self.cropplan:
            # print(self.cropplan.current_status)
          
        super(Task, self).save(*args, **kwargs)


from django.db import models
from .models_location import Location,Bed
from .models_botanical import Cultivar
from django.utils.text import slugify
from django.shortcuts import get_object_or_404
import datetime

class CropPlan(models.Model):

    cultivar = models.ForeignKey(Cultivar, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=60, blank=True)


    PLANTING_METHOD_CHOICES = [
        ('D', 'direct seeding'),
        ('T', 'transplanting'), 
    ]
    
    planting_method = models.CharField(max_length=1, choices=PLANTING_METHOD_CHOICES)

    STATUS_METHOD_CHOICES = [
        ('P', 'planned ⚪'),
        ('S', 'seedling house 🟡'),
        ('B', 'in bed 🟠'),
        ('H', 'harvestable 🟢'),
        ('T', 'terminated ⚫'),
    ]
    
    current_status = models.CharField(max_length=1, choices=STATUS_METHOD_CHOICES, default="('P', 'planned ⚪')",null=True, blank=True)
        
    location = models.ForeignKey(Location, on_delete=models.CASCADE, null=True,blank=True)

    beds = models.ManyToManyField(Bed, blank=True)


    date_of_planting = models.DateField()
    date_of_bed_preparation = models.DateField(null=True, blank=True)

    date_of_preseeding = models.DateField(null=True, blank=True)

    harvest_range_start_date = models.DateField(null=True, blank=True)
    harvest_range_end_date = models.DateField(null=True, blank=True)
    
    plating_distance_cm = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    num_rows = models.PositiveSmallIntegerField(blank=True, null=True)

    num_plants = models.PositiveSmallIntegerField(null=True,blank=True)

    amount_available_for_harvest = models.PositiveSmallIntegerField(null=True,blank=True)
  


    abandoned = models.BooleanField(default=False)
    abandonded_date = models.DateField(null=True, blank=True)
    abandonded_reason  = models.TextField(blank=True)

    notes  = models.TextField(blank=True)

    slug = models.CharField(max_length=60, blank=True,default='')


    verbose_name = models.CharField(max_length=60, blank=True)
    def __str__(self):
        return self.cultivar.name

    def create_task(self,task_type, task_date):
        from .models_task import Task

        new_task = Task(
            name = self.cultivar.name,
            due_date = task_date,
            task_type = task_type,
            cropplan = self,
            auto_created = True,
        )

     
        if self.location:
            new_task.location = self.location

        new_task.save()
        new_task.beds.set(self.beds.all())

    def save(self, *args, **kwargs):
        from .models_task import Task


        #### generate fields
        if self.product_name == None:
            self.product_name = self.cultivar.name  

        if self.plating_distance_cm == None:
            self.plating_distance_cm = self.cultivar.plating_distance_cm

        self.slug = slugify(self.cultivar.name) + str(self.id)


        #### generate dates

        if self.planting_method == 'T':
            if self.date_of_preseeding == None:
                self.date_of_preseeding = self.date_of_planting - datetime.timedelta(days=self.cultivar.days_seeding_to_transplatning)

        if self.harvest_range_start_date == None:
            self.harvest_range_start_date = self.date_of_planting + datetime.timedelta(days=self.cultivar.harvest_days_to_maturity_min)
        
        if self.harvest_range_end_date == None:
            self.harvest_range_end_date = self.date_of_planting + datetime.timedelta(days=self.cultivar.harvest_days_to_maturity_max)

        if self.date_of_bed_preparation == None:
            self.date_of_bed_preparation = self.date_of_planting - datetime.timedelta(days=14)

        super(CropPlan, self).save(*args, **kwargs)

        if self.num_rows == None and self.cultivar.num_rows != None:
            self.num_rows = self.cropplan.num_rows   

        if self.location and self.beds.exists():
            
            area = len(self.beds.all())*self.location.bed_length_meters
            distance = float(self.plating_distance_cm)*.01
            self.num_plants = area/distance
            
            super(CropPlan, self).save(*args, **kwargs)

        
        #### Task Creation ####
        auto_task_dictionary = {
            ('D', 'direct seeding'):[
                {
                    'type': 'D',
                    'due_date': self.date_of_planting
                }
            ],
            ('T', 'transplanting'):[
                {
                    'type': 'P',
                    'due_date': self.date_of_preseeding
                },
                {
                    'type': 'T',
                    'due_date': self.date_of_planting
                }
            ]
        }

        exisiting_tasks = Task.objects.all().filter(cropplan__id=self.id).filter(auto_created=True)

        if not exisiting_tasks:
            for planting_method, task_list in auto_task_dictionary.items():
                if self.planting_method == planting_method[0]:
                    for task in task_list:
                        self.create_task(task['type'], task['due_date'])
        else:
            for planting_method, task_list in auto_task_dictionary.items():
                if self.planting_method == planting_method[0]:
                    for task in task_list:
                        exisiting_task = exisiting_tasks.get(task_type=task['type'])
                        exisiting_task.due_date = task['due_date']

                       
                        if exisiting_task.beds.exists():
                            exisiting_task.beds.set(self.beds.all())

                        exisiting_task.location = self.location 
                     

                        exisiting_task.save()
    
    def get_next_task(self):
        # filter out completed tasks 

        if self.task_set.all():
            next_task = self.task_set.all().filter(completed=False).latest('-due_date')
            return next_task
        else:
            return None
            

                




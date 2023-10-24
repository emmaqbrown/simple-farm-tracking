import django_tables2 as tables
from .models_location import Location,Bed
from django_tables2.utils import A  # alias for Accessor
from django_tables2.utils import Accessor
from .models_crop_plan import CropPlan
from .models_task import Task
from .models_botanical import Species


class BedTable(tables.Table):
    # cropplan_set.all[0]= tables.Column(verbose_name='Employee name')
    cp = tables.ManyToManyColumn(CropPlan)
    name = tables.LinkColumn("bed", args=[A("name")],verbose_name="Bed")
    area_meters_squared = tables.Column(verbose_name='Area m^2')
    # cropplan = tables.LinkColumn("cropplan", args=[A("cropplan")],verbose_name="Bed")
  
    class Meta:
        model = Bed

        template_name = "django_tables2/bootstrap.html"

        fields = (
            "name", 
            "area_meters_squared",
            "active",
            "cropplan_set.all.0",
            "cropplan_set.all.0.get_current_status_display",
            "cp"
            )
        
        # cropplans = tables.ManyToManyColumn(transform=lambda user: u.name)




class TaskTableHtmx(tables.Table):
    cropplan = tables.LinkColumn("cropplans-detail", args=[A("cropplan.id")])
    name = tables.LinkColumn("task-detail", args=[A("id")],verbose_name="Task")

    class Meta:
        model = Task

        template_name = "farm_management_app/htmx_table.html"
        fields = (
            "name", 
            "due_date",
            "task_type",
            "location",
            "beds.all",
            "cropplan",
            "intended_amount_harvested",
            "actual_amount_harvested",
            "notes",
            "completed",
            )

class CropPlanTableHtmx(tables.Table):
   
    cultivar = tables.LinkColumn("cropplans-detail", args=[A("id")],verbose_name="cultivar")

    class Meta:
        model = CropPlan

        template_name = "farm_management_app/htmx_table.html"
        fields = (
            "cultivar", 
            "product_name",
            "cultivar.species",
            "cultivar.species.plant_family",
            "location",
            "date_of_planting",
            "current_status"
            )
        

class SpeciesTableHtmx(tables.Table):
   
    # species = tables.LinkColumn("cropplans-detail", args=[A("id")],verbose_name="cultivar")

    class Meta:
        model = Species

        template_name = "farm_management_app/htmx_table.html"
        fields = (
            "plant_family", 
            "alias_botanical_name",
            "common_name",
            "plant_type",
            "plating_distance_cm",
            "sowing_depth_cm",
            "temperture_germination",
            "days_seeding_to_transplatning",
            "num_rows"
            )




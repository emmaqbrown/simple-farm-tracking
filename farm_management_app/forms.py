from django.forms import ModelForm
from .models_task import Task
from .models_crop_plan import CropPlan
from .widgets import DatePickerInput

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name", 
            "due_date",
            "task_type",
            "location",
            "beds",
            "cropplan",
            "intended_amount_harvested",
            "notes",
            "completed"]

        widgets = {
            'due_date' : DatePickerInput()
        }

class TaskEditForm(ModelForm):
    class Meta:
        model = Task
        fields = [
            "name", 
            "due_date",
            "task_type",
            "location",
            "beds",
            "cropplan",
            "intended_amount_harvested",
            "actual_amount_harvested",
            "notes",
            "completed"]

        widgets = {
            'due_date' : DatePickerInput()
        }

class CropPlanForm(ModelForm):
    class Meta:
        model = CropPlan
        fields = [
            "cultivar", 
            "product_name",
            "planting_method",
            "current_status",
            "location",
            "beds",
            "date_of_planting",
            "date_of_bed_preparation",
            "date_of_preseeding",
            "harvest_range_start_date",
            "harvest_range_end_date",
            "plating_distance_cm",
            "notes",]


        help_texts = {
            "date_of_bed_preparation": ("not requied: will autofill 2 weeks prior to date of planning"),
            "date_of_preseeding": ("not requied: will autofill from crop plan"),
            "harvest_range_start_date": ("not requied: will autofill from crop plan"),
            "harvest_range_end_date": ("not requied: will autofill from crop plan"),
            "plating_distance_cm": ("not requied: will autofill from cultivar"),
        }

        widgets = {
            'date_of_planting' : DatePickerInput(),
            'date_of_bed_preparation' : DatePickerInput(),
            'date_of_preseeding' : DatePickerInput(),
            'harvest_range_start_date' : DatePickerInput(),
            'harvest_range_end_date' : DatePickerInput(),
        }
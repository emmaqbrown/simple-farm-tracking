from decimal import Decimal
from django.db.models import Q
import django_filters
from .models_location import Location, Bed
from .models_task import Task
from .models_crop_plan import CropPlan
from .models_botanical import Species

class TaskFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(field_name='location__name',lookup_expr='icontains')

    task_type = django_filters.CharFilter(field_name='task_type',lookup_expr='contains')
    # task_type = django_filters.MultipleChoiceFilter(field_name='task_type')

    completed = django_filters.BooleanFilter(field_name='completed')

    date_start = django_filters.DateFilter(field_name='due_date',lookup_expr='gte')
    date_end = django_filters.DateFilter(field_name='due_date',lookup_expr='lte')

    class Meta:
        model = Task
        fields = [
            'location', 
            'task_type',
            'completed',
            'date_start',
            'date_end'
            ]



class CropPlanFilter(django_filters.FilterSet):
    location = django_filters.CharFilter(field_name='location__name',lookup_expr='icontains')

    
    class Meta:
        model = CropPlan
        fields = [
            'location'
            ]

class SpeciesFilter(django_filters.FilterSet):
    # location = django_filters.CharFilter(field_name='location__name',lookup_expr='icontains')

    
    class Meta:
        model = Species
        fields = [
            'plant_family'
            ]

   



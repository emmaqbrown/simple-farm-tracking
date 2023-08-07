from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from .models_location import Location, Bed
from .models_crop_plan import CropPlan
from .models_botanical import Cultivar
from .models_task import Task
from django.core import serializers
from django.template import loader
from django_tables2 import SingleTableView, SingleTableMixin, RequestConfig
from .tables import BedTable,  TaskTableHtmx, CropPlanTableHtmx
from django_filters.views import FilterView
from .filters import TaskFilter, CropPlanFilter
from django.urls import reverse_lazy
from .forms import TaskForm, TaskEditForm, CropPlanForm
import datetime

# new cropplan - order by species common name 


# list of cultivars (info about cultivar, list of cropplans) (species, plantfamily details)
# non terminated crop plans 
# see multiple crop plans for 1 cultivar 
# history of crop plans

def index(request):
    template = "farm_management_app/index.html"

    return render(request, template)


def location_view(request):
    location_list = Location.objects.all()

    # only show in bed, harvest 
    # no seedling show - if it's actively in th ebed

    # show if 2 crop plans, e.g. green maure + crop
    
    location_bed_dict = {}
    for location in location_list:
        location_bed_dict[location] = location.bed_set.all()

    seedling_house_cropplans = CropPlan.objects.all().filter(current_status='S')

    template = "farm_management_app/location_list.html"
 
    context = {
        "location_bed_dict": location_bed_dict,
        "seedling_house_cropplans":seedling_house_cropplans
    }

    return render(request, template, context)


def bed_detail_view(request, bed_name):
    bed = get_object_or_404(Bed, name=bed_name)
  
    template = "farm_management_app/bed_detail.html"

    context = {
        "bed": bed,
        "tasks": bed.get_curr_year_tasks(),
        "cropplans_current_upcoming": bed.get_current_upcoming_cropplans(),
        "cropplans_historical": bed.get_historical_cropplans()
    }


    return render(request, template, context)



def cropplan_list(request):
    cropplan_list = CropPlan.objects.all()
    
    template = "farm_management_app/cropplan_list.html"
 
    context = {
        "cropplan_list": cropplan_list
        }

    return render(request, template, context)


def cropplan_new(request):
 
    template = "farm_management_app/basic_form.html"
    form = CropPlanForm(request.POST or None)

    context = {
            'title': 'New Crop Plan',

            'form': form
        }

    if request.method == 'POST':
        if form.is_valid():
            form_cleaned = form.cleaned_data
            form.save()
            
    
        return HttpResponseRedirect(reverse_lazy('cropplans-detail', args=[CropPlan.objects.all().last().id]))

    elif request.method == 'GET':
        return render(request, template, context)

def cropplan_detail_view(request, pk):
    cropplan = get_object_or_404(CropPlan, id=pk)

    template = "farm_management_app/cropplan_detail.html"

    context = {
        "cropplan": cropplan
    }

    return render(request, template, context)

def cropplan_edit_view(request, pk):
    cropplan = get_object_or_404(CropPlan, id=pk)

    template = "farm_management_app/basic_form.html"
  
    if request.method == 'POST':
        form = CropPlanForm(request.POST, instance = cropplan)

        if form.is_valid():
            form_cleaned = form.cleaned_data
            form.save()
    
        return HttpResponseRedirect(reverse_lazy('cropplans-detail', args=[CropPlan.objects.all().last().id]))

    elif request.method == 'GET':
        form = CropPlanForm(instance = cropplan)
        context = {
            'title': 'Crop Plan Edit',
            'form': form
            }
        return render(request, template, context)

class CropPlanTableHtmx(SingleTableMixin, FilterView):
    table_class = CropPlanTableHtmx
    queryset = CropPlan.objects.all().exclude(current_status='T').order_by('date_of_planting') 

    filterset_class = CropPlanFilter
    paginate_by = 20

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)

        context["locations"] = Location.objects.all()
        context["task_types"] = Task.TASK_TYPE_CHOICES
        context["completed_options"] = {
            'True': 'completed',
            'False': 'not completed'
        }

        curr_year = datetime.date.today().year
        context["date_after"] = str(datetime.date(curr_year, 1, 1))
        return context

    def get_template_names(self):

        if self.request.htmx:
            template_name = "farm_management_app/task_table_partial.html"
        else:
            template_name = "farm_management_app/cropplan_table_htmx.html"

        return template_name


class TaskTableHtmx(SingleTableMixin, FilterView):
    table_class = TaskTableHtmx
    queryset = Task.objects.all().exclude(task_type='H').order_by('due_date') 
    filterset_class = TaskFilter
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["locations"] = Location.objects.all()


        context["task_types"] =  [
            'transplant & direct seeding', 
            'pre-seeding', 
            'bed preparation',
            'terminate',
            'other'
            ]  
            
        context["completed_options"] = {
            'True': 'completed',
            'False': 'not completed'
        }

       
        return context

    def get_template_names(self):

        if self.request.htmx:
            template_name = "farm_management_app/task_table_partial.html"
        else:
            template_name = "farm_management_app/task_table_htmx.html"

        return template_name

def task_detail_view(request, pk):
    task = get_object_or_404(Task, id=pk)


    template = "farm_management_app/task_detail.html"

    context = {
        "task": task
    }

    return render(request, template, context)

def task_edit_view(request, pk):

    # compelte pre-seeding -> cropplna to 'seedling house'
    # complete direct seeding or transplating -> crop plan to 'in bed'

    # look at bed picking system for location 

    task = get_object_or_404(Task, id=pk)

    template = "farm_management_app/basic_form.html"
  
    if request.method == 'POST':
        form = TaskEditForm(request.POST, instance = task)

        if form.is_valid():
            form_cleaned = form.cleaned_data
            form.save()
    
        return HttpResponseRedirect(reverse_lazy('task-detail', args=[Task.objects.all().last().id]))

    elif request.method == 'GET':
        form = TaskEditForm(instance = task)
        context = {
                'title': 'Edit Task',
                'form': form
            }
        return render(request, template, context)

def task_complete(request, pk):
    task = get_object_or_404(Task, id=pk)

    if task.completed == True:
        task.completed = False
    else:
        task.completed = True
    task.save()

    return HttpResponseRedirect(reverse_lazy('task-detail', args=[pk]))

 
def new_task(request):
 
    template = "farm_management_app/basic_form.html"
    form = TaskForm(request.POST or None)

    context = {
            'title': 'New Task',

            'form': form
        }

    if request.method == 'POST':
        if form.is_valid():
            form_cleaned = form.cleaned_data
            form.save()
    
        return HttpResponseRedirect(reverse_lazy('task-detail', args=[Task.objects.all().last().id]))

    elif request.method == 'GET':
        return render(request, template, context)


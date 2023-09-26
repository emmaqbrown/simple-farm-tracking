from django.contrib import admin
from .models_botanical import PlantFamily, Species, Cultivar
from .models_location import Location, Bed
from .models_crop_plan import CropPlan
from .models_task import Task
from .models_user import User
from django.contrib.auth.admin import UserAdmin
from django import forms


admin.site.register(PlantFamily)


# class SpeciesForm(forms.ModelForm):
#     plant_family = forms.ModelChoiceField(queryset=PlantFamily.objects.order_by('botanical_name'))

#     class Meta:
#         model = Species

# class SpeciesAdmin(admin.ModelAdmin):
    # plant_family_ordering = "botanical_name"
    # ordering = [""]
    # fields = ["plant_family_display"]
    # list_display = ('plant_family')
    # form = SpeciesForm

    # ordering = ["plant_type"]


admin.site.register(Species)
admin.site.register(Cultivar)

######

class ChoiceInline(admin.TabularInline):
    model = Bed
    extra = 0


class LocationAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]



admin.site.register(Location, LocationAdmin)

######

admin.site.register(CropPlan)

######

admin.site.register(Task)
# admin.site.register(HarvestTask)


######

admin.site.register(User,UserAdmin)



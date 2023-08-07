from django.contrib import admin
from .models_botanical import PlantFamily, Species, Cultivar
from .models_location import Location, Bed
from .models_crop_plan import CropPlan
from .models_task import Task


admin.site.register(PlantFamily)
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





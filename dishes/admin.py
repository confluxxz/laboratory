from django.contrib.admin import site, ModelAdmin
from .models.dishes import Dishes

class DishesModelAdmin(ModelAdmin):
    pass

site.register(Dishes, DishesModelAdmin)
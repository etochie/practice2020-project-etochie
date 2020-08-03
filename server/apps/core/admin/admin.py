from django.contrib import admin

from apps.core.models import Cafe, Dish, Ingredient


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    pass


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    pass


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass

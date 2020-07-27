from django.contrib import admin

from apps.core.models import Cafe


@admin.register(Cafe)
class CafeAdmin(admin.ModelAdmin):
    pass

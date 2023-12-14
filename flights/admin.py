from django.contrib.admin import ModelAdmin, register
from .models import flight,Airport
@register(flight)
class flight_admin(ModelAdmin):
    autocomplete_fields=['origin']

@register(Airport)
class Airport_admin(ModelAdmin):
    list_display=("Name","No")
    search_fields=["Name"]
    list_filter=["Name","City"]



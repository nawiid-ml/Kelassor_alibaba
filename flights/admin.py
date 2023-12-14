from django.contrib.admin import ModelAdmin, register
from .models import flight,Airport
@register(flight)
class flight_admin(ModelAdmin):
    pass
@register(Airport)
class Airport_admin(ModelAdmin):
    pass



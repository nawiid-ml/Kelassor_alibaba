from django.contrib.admin import ModelAdmin, register
from .models import Train 

@register(Train)
class Train_admin(ModelAdmin):
    pass

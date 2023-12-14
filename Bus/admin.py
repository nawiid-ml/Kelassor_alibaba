from django.contrib.admin import ModelAdmin, register
from .models import Bus_Ticket,Terminal

@register(Bus_Ticket)
class Bus_Ticket_Admin(ModelAdmin):
    pass

@register(Terminal)
class Terminal_Admin(ModelAdmin):
    pass
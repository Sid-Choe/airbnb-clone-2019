from atexit import register
from django.contrib import admin
from . import models


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    """ Reservation Admin Definition """
    
    list_display = ("room", "check_in", "check_out", "guest", "status", "in_progress", "is_finish")

    list_filter = ("status",)

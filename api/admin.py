from django.contrib import admin
from .models import entry_status


class entry_status_Admin(admin.ModelAdmin):
    #todo: find on internet and change hostel to first_name
    list_display = ('user', 'show_tick')

admin.site.register(entry_status,entry_status_Admin)

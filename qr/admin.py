from django.contrib import admin
from .models import gate_entry

class EntryAdmin(admin.ModelAdmin):
    
    list_display = ('id','name', 'roomno', 'regno','outtime','intime')

admin.site.register(gate_entry,EntryAdmin)

# Register your models here.

from django.contrib import admin
from .models import user_profile


class UserAdmin(admin.ModelAdmin):
    #todo: find on internet and change hostel to first_name
    list_display = ('hostel', 'roomno', 'regno')

admin.site.register(user_profile,UserAdmin)


# Register your models here.

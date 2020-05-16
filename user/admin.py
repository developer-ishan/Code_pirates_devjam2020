from django.contrib import admin
from .models import user_profile,complaint


class UserAdmin(admin.ModelAdmin):
    #todo: find on internet and change hostel to first_name
    list_display = ('fullname', 'roomno', 'regno')
    def fullname(self, obj):
        return obj.user.get_full_name()

admin.site.register(user_profile,UserAdmin)

class complaintAdmin(admin.ModelAdmin):
    #todo: find on internet and change hostel to first_name
    list_display = ('firstname', 'desc', 'date','roomno','regno')
    def firstname(self, obj):
        return obj.sender.user.first_name
    def roomno(self, obj):
        return obj.sender.roomno
    def regno(self, obj):
        return obj.sender.regno
    
    list_filter = ['date', 'sender__roomno']
    

admin.site.register(complaint,complaintAdmin)


# Register your models here.

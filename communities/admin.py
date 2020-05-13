from django.contrib import admin
from .models import community,post
class communityAdmin(admin.ModelAdmin):
    
    list_display = ('name','admin')
class postAdmin(admin.ModelAdmin):
    
    list_display = ('community','created_at')

admin.site.register(community,communityAdmin)
admin.site.register(post,postAdmin)

# Register your models here.

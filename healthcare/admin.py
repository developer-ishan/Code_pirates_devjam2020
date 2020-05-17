from django.contrib import admin
from .models import doc,timing

# Register your models here.
class DesktopInline(admin.StackedInline):
    model = timing
    extra = 0


class SpecsAdmin(admin.ModelAdmin):
    inlines = [DesktopInline,]
admin.site.register(doc, SpecsAdmin)


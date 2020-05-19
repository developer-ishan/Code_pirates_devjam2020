from django.contrib import admin
from .models import doc,timing

# Register your models here.
class timingInline(admin.StackedInline):
    model = timing
    extra = 0


class SpecsAdmin(admin.ModelAdmin):
    inlines = [timingInline,]
admin.site.register(doc, SpecsAdmin)


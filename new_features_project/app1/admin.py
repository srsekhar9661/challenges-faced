from django.contrib import admin
from .models import Template


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'parent_template')
    search_fields = ('name',)
    list_filter =  ('parent_template',)


admin.site.register(Template, TemplateAdmin)

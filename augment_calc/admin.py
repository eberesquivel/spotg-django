from django.contrib import admin

from .models import *


class AdminAugment_Attribute(admin.ModelAdmin):
    list_display = ['id', 'description', 'type']


class AdminAugment_Skill(admin.ModelAdmin):
    list_display = ['id', 'name', 'attribute']


class AdminReporte(admin.ModelAdmin):
    list_display = ['augment_skill_id', 'attribute_description']


admin.site.register(Reporte, AdminReporte)
admin.site.register(Augment_Skill, AdminAugment_Skill)
admin.site.register(Augment_Attribute, AdminAugment_Attribute)

admin.site.site_header = "ReynalDev"

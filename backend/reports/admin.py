from django.contrib import admin

from .models import Report


class ReportAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'minimum_access_level',)


admin.site.register(Report, ReportAdmin)
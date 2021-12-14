from django.contrib import admin

from security.models import AlertLog


@admin.register(AlertLog)
class AlertLogAdmin(admin.ModelAdmin):
    readonly_fields = ('created_at',)


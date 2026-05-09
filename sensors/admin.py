from django.contrib import admin
from .models import Field, SensorData, IrrigationLog

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name', 'crop_type', 'area_size', 'created_at')
    search_fields = ('name', 'crop_type')

@admin.register(SensorData)
class SensorDataAdmin(admin.ModelAdmin):
    list_display = ('field', 'timestamp', 'temperature', 'humidity', 'soil_ph', 'light_intensity')
    list_filter = ('field', 'timestamp')
    date_hierarchy = 'timestamp'

@admin.register(IrrigationLog)
class IrrigationLogAdmin(admin.ModelAdmin):
    list_display = ('field', 'action_type', 'amount', 'timestamp')
    list_filter = ('action_type', 'field')
    date_hierarchy = 'timestamp'
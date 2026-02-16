from django.contrib import admin
from .models import ContentItem

# Uso de django.contrib.admin
@admin.register(ContentItem)
class ContentItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_by', 'created_at')
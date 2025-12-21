from django.contrib import admin
from .models import Tender

@admin.register(Tender)
class TenderAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')

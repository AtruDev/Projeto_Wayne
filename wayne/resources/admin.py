from django.contrib import admin
from .models import Resource

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
    list_display = ("nome", "tipo", "criado_em")
    search_fields = ("nome", "tipo")
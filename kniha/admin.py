from django.contrib import admin

from .models import Vzkaz


@admin.register(Vzkaz)
class VzkazAdmin(admin.ModelAdmin):
    list_display = ["jmeno", "text", "vytvoreno", "zverejneno"]
    list_filter = ["zverejneno"]
    list_editable = ["zverejneno"]
    search_fields = ["jmeno", "text"]

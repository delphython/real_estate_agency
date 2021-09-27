from django.contrib import admin

from .models import Flat
from .models import Complaint


class FLatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ["created_at",]
    list_display = ('address', 'price', 'new_building', 'construction_year',
        'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'compliant_text',)
    list_editable = ('flat', 'compliant_text',)
    raw_id_fields = ("flat",)


admin.site.register(Flat, FLatAdmin)
admin.site.register(Complaint, ComplaintAdmin)

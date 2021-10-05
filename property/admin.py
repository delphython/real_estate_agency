from django.contrib import admin

from .models import Complaint
from .models import Flat
from .models import Owner


class OwnerInline(admin.TabularInline):
    model = Owner.flat.through
    raw_id_fields = ("flat",)


class FLatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ["created_at",]
    list_display = ('address', 'price', 'new_building', 'construction_year',
        'town',)
    list_editable = ('new_building',)
    list_filter = ('new_building', 'rooms_number', 'has_balcony',)
    raw_id_fields = ("liked_by",)
    inlines = [OwnerInline,]


class ComplaintAdmin(admin.ModelAdmin):
    list_display = ('user', 'flat', 'compliant_text',)
    list_editable = ('flat', 'compliant_text',)
    raw_id_fields = ("flat",)


class OwnerAdmin(admin.ModelAdmin):
    list_display = ('owner', 'owners_phonenumber', 'owner_pure_phone',)
    list_editable = ('owners_phonenumber', 'owner_pure_phone',)
    raw_id_fields = ("flat",)
    inlines = [OwnerInline,]
    exclude = ('flat',)


admin.site.register(Flat, FLatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

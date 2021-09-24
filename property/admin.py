from django.contrib import admin

from .models import Flat


class FLatAdmin(admin.ModelAdmin):
    search_fields = ('town', 'address', 'owner',)
    readonly_fields = ["created_at",]


admin.site.register(Flat, FLatAdmin)

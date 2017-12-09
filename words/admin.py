from django.contrib import admin

from .models import Word


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    list_display = ('name', 'count')
    readonly_fields = ('name', 'count')
    list_display_links = None

    def has_add_permission(self, request):
        return False




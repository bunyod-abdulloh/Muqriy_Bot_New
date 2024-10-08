from django.contrib import admin
from .models import QuranAPD


class QuranAdmin(admin.ModelAdmin):
    actions_on_top = False
    list_display = ('sequence', 'sura_name',)
    ordering = ('sequence',)
    list_display_links = ('sura_name',)


admin.site.register(QuranAPD, QuranAdmin)
